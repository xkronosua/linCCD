#from pylab import *
import numpy as np
import serial
from time import sleep
import time
from serial.tools import list_ports

from PyQt4 import QtGui, QtCore
import pyqtgraph as pg

from Ui_CCD import Ui_CCD

def d4sigma(a):
	x = np.arange(len(a))
	a0 = np.mean([a[:200],a[-200:]])
	x0 = ((a-a0)*x).sum()/(a-a0).sum()
	return 4*np.sqrt(np.dot(a-a0,(x-x0)**2)/(a-a0).sum())



class CCDReader(QtGui.QWidget):
	ser = None
	line = None
	noDataN = 0
	port = '/dev/ttyUSB0'
	def __init__(self):
		super(CCDReader, self).__init__()

		# Set up the user interface from Designer.
		self.ui = Ui_CCD()
		self.ui.setupUi(self)
		self.show()
		self.pw = pg.PlotWidget(name='CCD')  
		
		self.ui.CCD_plot.addWidget(self.pw)

		self.line = self.pw.plot()
		self.line.setPen((200,200,100))
		self.pw.setYRange(0,65536)
		

		self.updateTimer = QtCore.QTimer()
		self.updateTimer.timeout.connect(self.updatePlot)
		self.ui.CCD_connect.toggled[bool].connect(self.connectClicked)
		self.ui.CCD_rec.toggled[bool].connect(self.recClicked)
		self.ui.pathSelect.clicked.connect(self.pathSelect)
		self.ui.filePath.textChanged[str].connect(self.checkPath)

	def checkPath(self,path):
		print(path)

	def recClicked(self,state):
		if state:
			self.ui.CCD_rec.setStyleSheet('background-color:red;')
			with open(self.ui.filePath.text(),'a') as f:
				f.write('#time\texposure\td4sigma\t'+"\t".join(np.arange(7296).astype(str))+"\n")
		else:
			self.ui.CCD_rec.setStyleSheet('background-color:#222222;')
	def pathSelect(self):
		fname = QtGui.QFileDialog.getSaveFileName(directory='./')
		print(fname)
		self.ui.filePath.setText(fname)

	def connectClicked(self, state):
		if state:

			ports = list(list_ports.grep("0403:6001"))
			self.port = '/dev/ttyUSB0'
			for i in ports:
				if i.description == 'TIT 2RCRP':
					self.port = i.device
			self.connect()
			

			trigger = self.ui.CCD_trigger.currentIndex()
			if trigger == 0:
				self.ser.write(b'#Text:0%'+bytearray([0x11,0x13]))
			elif trigger == 1:
				self.ser.write(b'#Text:1%'+bytearray([0x11,0x13]))
			
			integration_str = "#CCDInt:";
			
			integration = self.ui.CCD_exposure.value()
			if integration<=0 or integration>100:
					integration = 5
			str1 = ''
			if integration<10:
					str1="00"+str(integration)
			elif integration>=10 and integration<100:
					str1="0"+str(integration)
			elif integration==100:
					str1=str(integration);
			integration_str=integration_str+str1+"%";
			self.ser.write(integration_str.encode()+bytearray([0x11,0x13]))
			#r = self.ser.read(1)
			#n = self.ser.inWaiting()
			#r += ser.read(n)
			#print(r) 


			self.updateTimer.start(50)
		else:
			self.updateTimer.stop()
			self.disconnect()
	
	def updatePlot(self):
		self.updateTimer.stop()
		t = time.time()
		data = self.getData()
		print(time.time()-t,np.std(data-data.min()))
		self.line.setData(data)
		self.ui.D4Sigma.setText(str(np.round(d4sigma(data),2)))
		if self.ui.CCD_rec.isChecked():
			with open(self.ui.filePath.text(),'a') as f:
				out = "\t".join([str(time.time()), str(self.ui.CCD_exposure.value()),self.ui.D4Sigma.text()])
				out +="\t"+"\t".join(data.astype(str))+"\n"
				f.write(out)
		self.updateTimer.start(5)
		
	def connect(self):
		self.ser = serial.Serial(self.port,baudrate=921600,timeout=0.1, bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,rtscts=True,dsrdtr=True) 
	
	def disconnect(self):
		self.ser.close()
	
	def getData(self):
		ccd_vol_array = np.zeros(3648,dtype=int)
			
		if self.ser.isOpen():
			self.ser.write(b'#?data%'+bytearray([0x11,0x13]))
			sleep(0.01)
			read_buf = self.ser.read(7296)
			#sleep(0.05)
			#n=self.ser.inWaiting()
			#read_buf += self.ser.read(n)#4095)
			#sleep(0.05)
			#read_buf+=self.ser.read(1)
			#n1=self.ser.inWaiting()
			 
			#read_buf += self.ser.read(n1)#3200);
			kk=0;
			try:
				for i in range(0,8,2):
					if (read_buf[i]*256+read_buf[i+1])==24930: kk+=1
					if (read_buf[7288+i]*256+read_buf[7289+i])==24930: kk+=1
				if kk>=2:
					for i in range(0,7296,2):
						#print(i/2)
						ccd_vol_array[int(i/2)]=read_buf[i]*256+read_buf[i+1]
				else:
					for i in range(1,7295,2):
						ccd_vol_array[(i+1)/2]=read_buf[i]*256+read_buf[i+1]
				ccd_vol_array[0]=ccd_vol_array[1]=ccd_vol_array[2]=ccd_vol_array[3]=ccd_vol_array[4]=ccd_vol_array[5]
				ccd_vol_array[3647]=ccd_vol_array[3646]=ccd_vol_array[3645]=ccd_vol_array[3644]=ccd_vol_array[3643]
				#print(n,n1)
			except:
				print('noData')
				self.noDataN +=1
				if self.noDataN == 2:
					self.updateTimer.stop()
					#self.ui.CCD_connect.setChecked(False)
					self.disconnect()
					self.connect()
					self.ser.write(b'#Text:0%'+bytearray([0x11,0x13]))
					self.ser.write(b'#Text:1%'+bytearray([0x11,0x13]))
					self.noDataN = 0
		return ccd_vol_array


if __name__ == "__main__":
	import signal, sys
	#signal.signal(signal.SIGINT, sigint_handler)
	app = QtGui.QApplication(sys.argv)
	myWindow = CCDReader()
	app.exec_()
	#SMD_CloseComPort()
	print(":)")
	#os.kill(pid, signal.SIGTERM) #or signal.SIGKILL 

	sys.exit(1)
	'''
	plot()
	show(0)
	for i in range(10):
		t = time.time()
		r = proc_ccd()
		print(time.time()-t)
		plot(r)
		draw()
	show(0)
	
	ser.close()
	'''
