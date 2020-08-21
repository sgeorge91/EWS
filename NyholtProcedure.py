import numpy as np
import scipy as sp
import scipy.stats as spst
import scipy.linalg as spl
import math
import pandas as pd

#from ShannonJensen import SJ_ent
#fin=open("RN_Moovd_ud_WAff_WMean_WD2_WMPB_WSurr_WRP_WCorr_WAgeWtBMI.csv")#"ComplexityCatalog_v1.dat","r")
data=pd.read_csv("ConstRR_Results2_sinewn_shift2.dat", sep='\t')
cmat=np.zeros((7,7))
for i in range (0,7):
	cmat[i][i]=1
cmat[0][1]=cmat[1][0]=spst.pearsonr(data.det, data.lam)[0]
cmat[0][2]=cmat[2][0]=spst.pearsonr(data.det, data.lamdet)[0]
cmat[0][3]=cmat[3][0]=spst.pearsonr(data.det, data.lavg)[0]
cmat[0][4]=cmat[4][0]=spst.pearsonr(data.det, data.lent)[0]
cmat[0][5]=cmat[5][0]=spst.pearsonr(data.det, data.vavg)[0]
cmat[0][6]=cmat[6][0]=spst.pearsonr(data.det, data.vent)[0]
cmat[1][2]=cmat[2][1]=spst.pearsonr(data.lam, data.lamdet)[0]
cmat[1][3]=cmat[3][1]=spst.pearsonr(data.lam, data.lavg)[0]
cmat[1][4]=cmat[4][1]=spst.pearsonr(data.lam, data.lent)[0]
cmat[1][5]=cmat[5][1]=spst.pearsonr(data.lam, data.vavg)[0]
cmat[1][6]=cmat[6][1]=spst.pearsonr(data.lam, data.vent)[0]
cmat[2][3]=cmat[3][2]=spst.pearsonr(data.lamdet, data.lavg)[0]
cmat[2][4]=cmat[4][2]=spst.pearsonr(data.lamdet, data.lent)[0]
cmat[2][5]=cmat[5][2]=spst.pearsonr(data.lamdet, data.vavg)[0]
cmat[2][6]=cmat[6][2]=spst.pearsonr(data.lamdet, data.vent)[0]
cmat[3][4]=cmat[4][3]=spst.pearsonr(data.lavg, data.lent)[0]
cmat[3][5]=cmat[5][3]=spst.pearsonr(data.lavg, data.vavg)[0]
cmat[3][6]=cmat[6][3]=spst.pearsonr(data.lavg, data.vent)[0]
cmat[4][5]=cmat[5][4]=spst.pearsonr(data.lent, data.vavg)[0]
cmat[4][6]=cmat[6][4]=spst.pearsonr(data.lent, data.vent)[0]
cmat[5][6]=cmat[6][5]=spst.pearsonr(data.vavg, data.vent)[0]
print cmat

b=spl.eigvals(abs(cmat))
print b
bvar=np.var(b)
meff=1+((6)*(1-(bvar/7)))
print meff
