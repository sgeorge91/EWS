import pymannkendall as mk
import numpy as np
import scipy.stats as ss
fin=open("ConstRR_Results2_10min_JD_2186_PreTrans.csv","r")
a=fin.readlines()
temp=""
temp1=np.zeros(len(a))
temp2=np.zeros(len(a))
temp3=np.zeros(len(a))
temp4=np.zeros(len(a))
#temp5=np.zeros(len(a))

for i in range (1,len(a)):
	temp=a[i].split()
	temp1[i]=float(temp[0])
	temp2[i]=float(temp[4])
	temp3[i]=float(temp[3])
	temp4[i]=float(temp[2])
	#temp5[i]=float(temp[4])
	

kt,pkt=ss.kendalltau(temp1,temp2)
print ("Kendall tau and pvalue are", kt,pkt)
result=mk.hamed_rao_modification_test(temp2)
print(result, "RR")
kt,pkt=ss.kendalltau(temp1,temp3)
print ("Kendall tau and pvalue are", kt,pkt)
result=mk.hamed_rao_modification_test(temp3)
print(result, "Det")
kt,pkt=ss.kendalltau(temp1,temp4)
print ("Kendall tau and pvalue are", kt,pkt)
result=mk.hamed_rao_modification_test(temp4)
print(result, "Lam")
#result=mk.hamed_rao_modification_test(temp5)
#print(result, "ratio")
