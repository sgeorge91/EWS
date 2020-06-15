import numpy as np
def acf1(t,x,bs):
	mx=np.mean(x)
	denom=0.
	rk=0.
	dis=bs
	ctr=0
	size=[]
	x=[p-mx for p in x]
	ctrg=0
	xp=[]
	l=1
	for i in range (0,len(x)-l):
		size.append(t[i+l]-t[i])
		if(t[i+l]-t[i]<=dis+(bs/2.)):
			xp.append(x)
			rk=rk+((x[i])*(x[i+l]))
			ctr=ctr+1
		denom=denom+(x[i]*x[i])
	rk=rk/denom
	return (rk)
def ar1(x0,rk,var):
	sd=np.sqrt(var)
	return rk*x0+np.random.normal(0,sd)
def acf1surr(t,x,bs):
	import random
	rk=acf1(t,x,bs)
	l1=len(x)
	var_s=np.var(x)
	var_n=(1-rk**2)*var_s
	x0=random.choice(x)
	x1=np.zeros(l1)
	x1[0]=x0
	for i in range (1,l1):
		x1[i]=(ar1(x0,rk,var_n))
	return x1
	
			

