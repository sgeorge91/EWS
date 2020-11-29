#Finds the recurrence plots a time series in a moving window and writes the results of the moving window into a separate file
import numpy as np
import math
import time as tm
import os
from numpy import conjugate,absolute
import pandas as pd
fn="10min_JD_2186_PreTrans.csv"
b=pd.read_csv(fn,delimiter='\t')
l1=len(b)
print b.head()
print "Length of file is",len(b)
fout_sig=open("ConstRR_Results2_"+fn,"w") #Results file
leng=2016 #window size
wsd=14#window size in days
t0=b.loc[0,"Time"]
sp=b.shape[0]-1
print sp, "is shapy"
tend=b.loc[sp,"Time"]
flag=True
flag1=True
i=0
fout_sig.write('winno\teps\trr\tdet\tlam\tdetrr\tlamdet\tlavg\tlent\tvavg\tvent')
while(flag1==True):
	i=i+1
	flag=True
	a=b[(b["Time"]>t0)&(b["Time"]<t0+wsd)]
	print "Yo",a.head()	
	a=np.array(a["Amp"])
	print type(a[1]), a[1]
	np.savetxt('junk.dat',a, delimiter ='\t')
	leng=len(a)
	epsilon=.005
	fn1="ud_junk.dat"
	udc="u" #This option is brought forward from a previous version that had an option to not have uniform deviates
	if(udc=="u")or(udc=="U"):
		os.system ("./UD.out junk.dat"+" "+str(leng))
		fn1="ud_junk.dat"
	ctr_e=1
	print fn1, "reached here"
	while(flag==True):
		
		os.system("./rp -i ud_junk.dat -o RQA_"+fn1+" -m 1 -e "+str(ctr_e*epsilon))
		fin2=open("RQA_"+fn1)
		rpm=fin2.readlines()
		rpm2=rpm[1].split()
		ctr_e=ctr_e+1	
		if(float(rpm2[0])<.05):
			print rpm2[0]
			os.remove("RQA_"+fn1)									
			continue
			
		else:			
			flag=False

	print "Breakout!",i
	fout_sig.write(str(i)+'\t'+str(ctr_e*epsilon)+'\t'+rpm2[0]+'\t'+rpm2[1]+'\t'+rpm2[3]+'\t'+rpm2[2]+'\t'+rpm2[4]+'\t'+rpm2[6]+'\t'+rpm2[7]+'\t'+rpm2[10]+'\t'+rpm2[11]+'\n')
	fin2.close()
	os.rename("RQA_"+fn1,"./RQARR5/RQA_"+fn1+"_"+str(i))
	t0=t0+0.125
	if(t0+wsd>tend):
		flag1=False
fout_sig.close()
