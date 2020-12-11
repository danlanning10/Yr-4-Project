# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 17:10:07 2020

@author: danla
"""
import numpy as np

time=[]
flux=[]
lum=[]
err_lum=[]
fluxerr=[]
mjd=[]
mags=[]
errors=[]

with open("AT2019mha_lc_noheaders.txt", 'r') as file:
    txt=file.read().replace(',,', '')
    
with open("AT2019mha_lc_noheaders.txt", 'w') as file:
    file.write(txt)    

with open("AT2019mha_lc_noheaders.txt") as file:
    for line in file:
        data = line.split(',')
        time.append(data[0])
        flux.append(data[2])
        fluxerr.append(data[3])
        lum.append(data[4])
        err_lum.append(data[5])

#print(time)
       

#print(lum)    
#print(time)

for i in range(len(time)):
    mjd.append(float(time[i])+58703.80)
for i in range(len(flux)):
    mags.append(-2.5*np.log10(float(flux[i])/3631))
for i in range(len(lum)):
    errors.append(0.434*(float(err_lum[i])/float(lum[i])))


mjdw2 = mjd[0:3]
magw2 = mags[0:3]
errw2 = errors[0:3]

mjdm2 = mjd[3:6]
magm2 = mags[3:6]
errm2 = errors[3:6]

mjdw1 = mjd[6:9]
magw1 = mags[6:9]
errw1 = errors[6:9]
'''
mjdu = mjd[21:24]
magu = mags[21:24]
erru = errors[21:24]

mjdu_IOO = mjd[24:26]
magu_IOO = mags[24:26]
erru_IOO = errors[24:26]

mjdb = mjd[111:122]
magb = mags[111:122]
errb = errors[111:122]
'''
mjdg_IOO = mjd[9:10]
magg_IOO = mags[9:10]
errg_IOO = errors[9:10]

mjdg = mjd[10:54]
magg = mags[10:54]
errg = errors[10:54]
'''
mjdr_SEDM = mjd[130:131]
magr_SEDM = mags[130:131]
errr_SEDM = errors[130:131]
'''
mjdr_IOO = mjd[54:55]
magr_IOO = mags[54:55]
errr_IOO = errors[54:55]

mjdr = mjd[55:]
magr = mags[55:]
errr = errors[55:]
'''
mjdi_IOO = mjd[204:205]
magi_IOO = mags[204:205]
erri_IOO = errors[204:205]

mjdi = mjd[205:]
magi = mags[205:]
erri = errors[205:]
'''


with open("AT2019mha_machinereadable.txt", "w") as file:    
    for i in range(len(mjdw2)):
        file.write(f"{mjdw2[i]},{magw2[i]},{errw2[i]},SWIFT,w2\n")
    for i in range(len(mjdm2)):
        file.write(f"{mjdm2[i]},{magm2[i]},{errm2[i]},SWIFT,m2\n")
    for i in range(len(mjdw1)):
        file.write(f"{mjdw1[i]},{magw1[i]},{errw1[i]},SWIFT,w1\n")
    #for i in range(len(mjdb)):
     #   file.write(f"{mjdb[i]},{magb[i]},{errb[i]},SWIFT,b\n")
    #for i in range(len(mjdu)):
     #   file.write(f"{mjdu[i]},{magu[i]},{erru[i]},SWIFT,u\n")
    #for i in range(len(mjdu_IOO)):
     #   file.write(f"{mjdu_IOO[i]},{magu_IOO[i]},{erru_IOO[i]},IOO,u\n")    
    for i in range(len(mjdg_IOO)):
        file.write(f"{mjdg_IOO[i]},{magg_IOO[i]},{errg_IOO[i]},IOO,g\n")
    for i in range(len(mjdg)):
        file.write(f"{mjdg[i]},{magg[i]},{errg[i]},ZTF,g\n")
    for i in range(len(mjdr_IOO)):
        file.write(f"{mjdr_IOO[i]},{magr_IOO[i]},{errr_IOO[i]},IOO,r\n")    
    for i in range(len(mjdr)):
        file.write(f"{mjdr[i]},{magr[i]},{errr[i]},ZTF,r\n") 
    #for i in range(len(mjdr_SEDM)):
     #   file.write(f"{mjdr_SEDM[i]},{magr_SEDM[i]},{errr_SEDM[i]},SEDM,r\n")
    #for i in range(len(mjdi_IOO)):    
     #   file.write(f"{mjdi_IOO[i]},{magi_IOO[i]},{erri_IOO[i]},IOO,i\n")  
    #for i in range(len(mjdi)):    
     #   file.write(f"{mjdi[i]},{magi[i]},{erri[i]},ZTF,i\n")    

#print(flux)        
