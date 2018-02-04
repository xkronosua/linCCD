#from pylab import *
import numpy as np
import serial
from time import sleep
import time
from serial.tools import list_ports

from PyQt4 import QtGui, QtCore
import pyqtgraph as pg

from Ui_CCD import Ui_CCD

from TCD1304 import TCD1304

def d4sigma(a,bg=[]):
	a = a[300:-300]
	x = np.arange(len(a))
	if len(bg)==0:
		a0 = np.mean([a[:200],a[-200:]])
	else:
		a = a-bg[:len(a)]
		a0 = min(a)
	x0 = ((a-a0)*x).sum()/(a-a0).sum()
	#print(x0,a0)
	return 4*np.sqrt(np.dot(abs(a-a0),(x-x0)**2)/abs(a-a0).sum())



class CCDReader(QtGui.QWidget):
	ser = None
	line = None
	baseline = None
	noDataN = 0
	port = '/dev/ttyUSB0'
	rec_counter = 0
	CCD = None
	bg = []
	lastTime = time.time()
	def __init__(self):
		super(CCDReader, self).__init__()

		# Set up the user interface from Designer.
		self.ui = Ui_CCD()
		self.ui.setupUi(self)
		self.show()
		self.pw = pg.PlotWidget(name='CCD')

		self.ui.CCD_plot.addWidget(self.pw)

		self.line = self.pw.plot()
		self.baseline = self.pw.plot()

		self.line.setPen((200,200,100))
		self.baseline.setPen((200,0,255))
		
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
			self.rec_counter = 0;
			self.ui.CCD_rec.setStyleSheet('background-color:red;')
			with open(self.ui.filePath.text(),'a') as f:
				f.write('#time\texposure\td4sigma\t'+"\t".join(np.arange(3648).astype(str))+"\n")
		else:
			self.ui.CCD_rec.setStyleSheet('background-color:#222222;')
	def pathSelect(self):
		fname = QtGui.QFileDialog.getSaveFileName(directory='./')
		print(fname)
		self.ui.filePath.setText(fname)

	def connectClicked(self, state):
		if state:

			'''

			self.CCD = TCD1304(trigger=False,
				integration=self.ui.CCD_exposure.value())
			self.CCD.start()
			
			time.sleep(3)
			data_list = []
			min_sum = 3647*65000
			min_sum_index = 0
			n = 0

			while not self.CCD.data_q.empty():
				data = self.CCD.data_q.get()[0]
				print(data.sum())
				if data.sum()<min_sum:
					min_sum_index = n
					min_sum = data.sum()

				data_list.append(data)
				n+=1
				print(n,min_sum_index,min_sum)
			print('min:',min_sum_index)
			self.bg = data_list[min_sum_index]
			self.baseline.setData(self.bg)
			
			self.CCD.stop()
			'''
			self.CCD = TCD1304(trigger=self.ui.CCD_trigger.currentIndex(),
				integration=self.ui.CCD_exposure.value())
			self.CCD.start()
			if not self.CCD.error_q.empty():
				print(self.CCD.error_q.get())
				self.CCD.stop()
				self.ui.CCD_connect.setStyleSheet('background-color:#222222;')
				self.ui.CCD_connect.setChecked(False)
			else:
				self.updateTimer.start(500)
				self.ui.CCD_connect.setStyleSheet('background-color:green;')
		else:
			self.updateTimer.stop()
			self.CCD.stop()
			self.ui.CCD_connect.setStyleSheet('background-color:#222222;')

	def updatePlot(self):
		#self.updateTimer.stop()
		tDiff = time.time() - self.lastTime
		self.lastTime = time.time()
		print('tDiff:\t',tDiff)
		t = time.time()
		if not self.CCD.error_q.empty():
			self.CCD.stop()
			self.ui.CCD_connect.setStyleSheet('background-color:#222222;')
			self.ui.CCD_connect.setChecked(False)
			
			while not self.CCD.error_q.empty():
				err = self.CCD.error_q.get()
				print(err)	
				
				#if err[:11] == 'read failed':
					#time.sleep(3)
					#while not self.CCD.error_q.empty():
					#	err = self.CCD.error_q.get()
			
					#self.CCD = TCD1304(trigger=self.ui.CCD_trigger.currentIndex(),
					#	integration=self.ui.CCD_exposure.value())
					#self.CCD.start()
					#self.ui.CCD_connect.setStyleSheet('background-color:green;')
					#self.ui.CCD_connect.setChecked(True)
					
				'''
				while not self.CCD.error_q.empty():
					err = self.CCD.error_q.get()
					print(err)
					self.CCD.stop()
					self.ui.CCD_connect.setStyleSheet('background-color:#222222;')
					self.ui.CCD_connect.setChecked(False)
					self.updateTimer.stop()
				'''
			return	

		stack = []#self.CCD.data_q.get()[0]
		cn = 0
		while not self.CCD.data_q.empty():
			stack.append( self.CCD.data_q.get()[0])
			cn += 1
		if len(stack)==0: return
		data = np.sum(stack,axis=0)/(cn+1)
		if sum(data)==0:
			self.CCD.stop()
			self.CCD = TCD1304(trigger=False,
				integration=self.ui.CCD_exposure.value())
			print('Trigger: Int.')
			self.CCD.start()
			time.sleep(0.2)
			self.CCD.stop()
			self.CCD = TCD1304(trigger=self.ui.CCD_trigger.currentIndex(),
				integration=self.ui.CCD_exposure.value())
			self.CCD.start()
			print('Trigger: Ext.')
			
		print("#",cn,cn/tDiff)
		d4s = d4sigma(data,bg = self.bg)
		#print(time.time()-t,d4s)
		self.line.setData(data)
		
		try:
			self.ui.D4Sigma.setText(str(int(d4s)))
		except ValueError:
			self.ui.D4Sigma.setText("nan")
		if self.ui.CCD_rec.isChecked():
			self.rec_counter += 1
			self.ui.rec_counter.setText(str(self.rec_counter))

			with open(self.ui.filePath.text(),'a') as f:
				out = "\t".join([str(time.time()), str(self.ui.CCD_exposure.value()),self.ui.D4Sigma.text()])
				out +="\t"+"\t".join(data.astype(str))+"\n"
				f.write(out)
			if self.rec_counter >= self.ui.rec_limit.value():
				self.ui.CCD_rec.setChecked(False)
				self.recClicked(False)
		if self.ui.CCD_baseline.isChecked():
			time.sleep(1)
			data_list = []
			min_sum = 3647*65000
			min_sum_index = 0
			n = 0
			if len(self.bg)==0:
				self.bg = self.CCD.data_q.get()[0]
			min_sum = self.bg.sum()
			while not self.CCD.data_q.empty():
				data = self.CCD.data_q.get()[0]
				#print(data.sum())
				if data.sum()<min_sum:
					min_sum_index = n
					min_sum = data.sum()

				data_list.append(data)
				n+=1
				print(n,min_sum_index,min_sum)
			print('min:',min_sum_index)
			self.bg = data_list[min_sum_index]
			self.baseline.setData(self.bg)
		#self.updateTimer.start(200)

	
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
