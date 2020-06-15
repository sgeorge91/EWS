####Created by Sandip Varkey George####
###contains functions to generate ar1 surrogates###

import numpy as np
##The acf1 fucntion takes the time array, response array and bin size (sampling time) 
##as the input variables and returns the autocorelation at lag 1
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
##ar1 returns the next value in an ar1 process when the previous value, correlation coefficient and variance are entered 
def ar1(x0,rk,var):
	sd=np.sqrt(var)
	return rk*x0+np.random.normal(0,sd)
##acf1surrogates accepts a time series with seperate time and amplitude inputs and returns a surrogate dataset with 
##the same autocorrelation at lag 1 and varaince structure as the original time series
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
	
			

