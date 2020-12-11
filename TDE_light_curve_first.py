# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 15:28:48 2020

@author: danla
"""

import numpy as np
import matplotlib.pyplot as plt

time=[]
mag= []
e_mag = []

with open("AT2019qiz-mr-phot-easyread.txt") as file:
    for wv in file:
        rv=wv.split()
        time.append(float(rv[0]))
        mag.append(float(rv[1]))
        e_mag.append(float(rv[2]))
        
time_r=time[0:59]
mag_r=mag[0:59]
e_mag_r=e_mag[0:59]

time_g=time[60:113]
mag_g=mag[60:113]
e_mag_g=e_mag[60:113]

time_i=time[114:141]
mag_i = mag[114:141]
e_mag_i = e_mag[114:141]

time_c = time[142:156]
mag_c = mag[142:156]
e_mag_c = e_mag[142:156]

time_o = time[143:199]
mag_o = mag[143:199]
e_mag_o = e_mag[143:199]

time_u = time[200:227]
mag_u = mag[200:227]
e_mag_u = e_mag[200:227]

time_w1 = time[228:264]
mag_w1 = mag[228:264]
e_mag_w1 = e_mag[228:264]

time_m2 = time[265:288]
mag_m2 = mag[265:288]
e_mag_m2 = e_mag[265:288]

time_w2 = time[289:314]
mag_w2 = mag[289:314]
e_mag_w2 = e_mag[289:314]

print(mag_i) 
plt.figure(figsize=(8,5.5))
plt.tick_params(axis = 'both', labelsize='30')
plt.gca().invert_yaxis()
plt.ylabel('Apparent magnitude', fontsize='30')
plt.xlabel('Time [MJD]', fontsize='30')
plt.title('Light Curve for TDE AT2019qiz', fontsize='30')
plt.errorbar(time_r, mag_r, xerr=None, yerr=e_mag_r, fmt='r.', label='R-band')
plt.errorbar(time_g, mag_g, xerr=None, yerr=e_mag_g, fmt='g.', label='G-band')
plt.errorbar(time_i, mag_i, xerr=None, yerr=e_mag_i, fmt='y.', label='I-band')
plt.errorbar(time_c, mag_c, xerr=None, yerr=e_mag_c, fmt='c.', label='C-band')
plt.errorbar(time_o, mag_o, xerr=None, yerr=e_mag_o, fmt='b.', label='O-band')
plt.errorbar(time_u, mag_u, xerr=None, yerr=e_mag_u, fmt='m.', label='U-band')
plt.errorbar(time_w1, mag_w1, xerr=None, yerr=e_mag_w1, fmt='.', color='pink', label='W1 band')
plt.errorbar(time_m2, mag_m2, xerr=None, yerr=e_mag_m2, fmt='.', color='darkslategray', label='M2 band')
plt.errorbar(time_w2, mag_w2, xerr=None, yerr=e_mag_w2, fmt='.', color='chocolate', label='W2 band')
plt.legend(fontsize='18')
plt.show()
