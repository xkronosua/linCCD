from pylab import *
from lmfit.models import GaussianModel, ConstantModel
import sys
fname = sys.argv[1]
data = loadtxt(fname)
res = []
n = round(len(data)**0.5)
m = n+1
for j,d in enumerate(data):
	sigma = d[2]
	y = d[3:]
	x = arange(len(y))
	y0 = np.mean([y[:200],y[-200:]])
	x0 = ((y-y0)*x).sum()/(y-y0).sum()
	mod = GaussianModel()

	pars = mod.guess(y, x=x)
	pars['sigma'].set(sigma,min=5,max=4000)
	pars['center'].set(x0,min=200,max=6500)
	#pars['amplitude'].set(y.max()/sigma,min=1,max=60536)
	bg = ConstantModel()
	pars.update(bg.make_params())
	pars['c'].set(y.min())
	
	model = mod + bg
	
	out  = model.fit(y, pars, x=x)
	print(out.fit_report(min_correl=0.25))
	ax=subplot(n,m,j+1)
	ax.tick_params(labelbottom='off')   
	ax.tick_params(labelleft='off')   
	plot(x,y,'ob')
	plot(x,out.best_fit,'-r')
	res.append(out.params)

keys=list(res[0].keys())

header =[]
for k in keys:
	header.append(k)
	header.append(k+"_stderr")


import pandas as pd 

data = []
for r in res:
	tmp=[]
	for k in keys:
		tmp.append(r[k].value)
		tmp.append(r[k].stderr)
	data.append(tmp)

data = array(data)

df = pd.DataFrame(data,columns=header)
df.to_csv(fname+"_res.dat",sep='\t')
show(0)

# sigma -- diameter!!!!!!!!!!!!!!!!!!!!!!!!!