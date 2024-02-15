# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 17:15:31 2021

@author: Ashwin
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import periodogram
import allantools as adev

filename1 = 'XX.S0001..HHX_centaur-6_8725_20230217_080000' #enter the file name here
filename2 = 'XX.S0001..HHY_centaur-6_8725_20230217_080000'
filename3 = 'XX.S0001..HHZ_centaur-6_8725_20230217_080000'
label1 = 'stabilized'


label2 = 'not stabilized'

plot_name = 'noperturbation_Comparision_asd'

sampling_rate = 100
###############################################################################

# raw = np.loadtxt(filename, unpack = True) 
# print(data)

data_raw1 = open(filename1 + '.txt', 'r')
data_raw2 = open(filename2 + '.txt', 'r')
data_raw3 = open(filename3 + '.txt', 'r')
data1 = []
data2 = []
data3 = []


for line in data_raw1:
    line = line.strip()
    line = line.replace(',', '.')
    line = line.split('\t')
    data1.append(line) 
for line in data_raw2:
    line = line.strip()
    line = line.replace(',', '.')
    line = line.split('\t')
    data2.append(line) 
for line in data_raw3:
    line = line.strip()
    line = line.replace(',', '.')
    line = line.split('\t')
    data3.append(line) 
data1 = np.array(data1[:])
data2 = np.array(data2[:])
data3 = np.array(data3[:])


data11 = np.array(data1[:,1],dtype=float)
data12 = np.array(data2[:,1],dtype=float)
data13 = np.array(data3[:,1],dtype=float)
for  i in range(len(data12)):
    data11[i]=data11[i]/(6)
    data12[i]=data12[i]/(6)
    data13[i]=data13[i]/(6)
accn1 = np.gradient(data11)
accn2 = np.gradient(data12)
accn3 = np.gradient(data13)


dis1 = np.zeros(len(data11))
dis2 = np.zeros(len(data12))
dis3 = np.zeros(len(data13))

for  i in range(len(data12)-1):

    dis1[i] = (data11[i+1]+data11[i])/200
    dis2[i] = (data12[i+1]+data12[i])/200
    dis3[i] = (data13[i+1]+data13[i])/200










t = np.linspace(1/sampling_rate, len(data1)/sampling_rate, len(data1))









f1, p1 = periodogram(accn1, sampling_rate)


f2, p2 = periodogram(accn2, sampling_rate)
f3, p3 = periodogram(accn3, sampling_rate)
window = 20

average_p1 = []
average_p2 = []
average_p3 = []
avg_f = []
for ind in range(len(p1) - window + 1):
     average_p1.append(np.mean(p1[ind:ind+window]))
     average_p2.append(np.mean(p2[ind:ind+window]))
     average_p3.append(np.mean(p3[ind:ind+window]))
     avg_f.append(np.mean(f1[ind:ind+window]))




#fig, axs = plt.subplots(2,2,num='plot',figsize=(12,12)) 
#fig.suptitle('Reference (Y-axis) ')



#axs[0, 1].cla()
#axs[0, 1].set_title('Acceleration spectral density')

#axs[0, 1].semilogy(avg_f, np.sqrt(average_p1)/(1000000), 'r-',label='', alpha = 0.75)
#axs[0, 1].semilogy(avg_f, np.sqrt(average_p2)/(1000000), 'g-',label='', alpha = 0.75)
#axs[0, 1].semilogy(avg_f, np.sqrt(average_p3)/(1000000), 'b-',label='', alpha = 0.75)
#axs[0, 1].set_xlim(0,30)
#axs[0, 1].set_ylim(1e-8,1e-2)
#axs[0, 1].legend()
#axs[0, 1].grid()
#axs[0, 1].set(xlabel = 'frequency [Hz]', ylabel = 'ASD')
plt.figure('time-series-relative')
plt.clf() 
plt.semilogy(avg_f, np.sqrt(average_p1)/(1000000), 'r-',label='', alpha = 0.75)
plt.semilogy(avg_f, np.sqrt(average_p2)/(1000000), 'g-',label='', alpha = 0.75)

plt.semilogy(avg_f, np.sqrt(average_p3)/(1000000), 'b-',label='', alpha = 0.75)
plt.legend()
plt.grid()
plt.xlim(0,30)
plt.ylim(1e-8,1e-2)
plt.xlabel('frequency [Hz]')
plt.ylabel('ASD [SI unit]')







plt.savefig(plot_name + '.png')
plt.show()




