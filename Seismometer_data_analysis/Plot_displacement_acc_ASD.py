# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 17:15:31 2021

@author: Ashwin
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import periodogram
import allantools as adev

filename1 = 'XX.S0001..HHY_centaur-6_8725_20230217_080000' #enter the file name here
label1 = 'stabilized'

filename2 = filename1
label2 = 'not stabilized'

plot_name = filename1

sampling_rate = 100
###############################################################################

# raw = np.loadtxt(filename, unpack = True) 
# print(data)

data_raw = open(filename1 + '.txt', 'r')
data = []


for line in data_raw:
    line = line.strip()
    line = line.replace(',', '.')
    line = line.split('\t')
    data.append(line) 
data = np.array(data[:])


data1 = np.array(data[:,1],dtype=float)
for  i in range(len(data1)):
    data1[i]=data1[i]/(6)
accn = np.gradient(data1)
dis = np.zeros(len(data1))

for  i in range(len(data1)-1):

    dis[i] = (data1[i+1]+data1[i])/200










t = np.linspace(1/sampling_rate, len(data1)/sampling_rate, len(data1))

mean1 = np.mean(data1)

std1 = np.std(data1)
std2 = np.std(data1)

fluct1 = np.multiply(np.subtract(np.divide(data1, mean1),1),100)
fluct2 = np.multiply(np.subtract(np.divide(data1, mean1),1),100)



(tau1, adev1, adev1err, n) = adev.adev(data1, rate=sampling_rate, data_type="freq", taus=None)
(tau2, adev2, adev2err, n) = adev.adev(data1, rate=sampling_rate, data_type="freq", taus=None)


f1, p1 = periodogram(accn, sampling_rate)


f2, p2 = periodogram(accn, sampling_rate)
window = 20
y=p1
average_y = []
avg_x = []
for ind in range(len(y) - window + 1):
     average_y.append(np.mean(y[ind:ind+window]))
     avg_x.append(np.mean(f1[ind:ind+window]))




fig, axs = plt.subplots(2,2,num='plot',figsize=(12,12)) 
fig.suptitle('Reference (Y-axis) ')


axs[0, 0].cla()
axs[0, 0].set_title('Velocity vs. Time') 
axs[0, 0].plot(t, data1, 'g-', label = '', alpha = 0.75)
axs[0, 0].legend()
axs[0, 0].grid()
axs[0, 0].set(xlabel = 'time [s]', ylabel = 'Velocity [\u03BCm/s]')
axs[0, 1].cla()
axs[0, 1].set_title('Acceleration spectral density')
#axs[0, 1].semilogy(f2, np.sqrt(p2)/(1000000), 'r-',label='', alpha = 0.75)
axs[0, 1].semilogy(avg_x, np.sqrt(average_y)/(1000000), 'g-',label='', alpha = 0.75)
axs[0, 1].set_xlim(0,30)
axs[0, 1].set_ylim(1e-8,1e-2)
axs[0, 1].legend()
axs[0, 1].grid()
axs[0, 1].set(xlabel = 'frequency [Hz]', ylabel = 'ASD')
axs[1, 0].cla()
axs[1, 0].set_title('Acceleration vs. Time')

axs[1, 0].plot(t,accn, 'g-',label='', alpha = 0.75)

axs[1, 0].legend()
axs[1, 0].grid()
axs[1, 0].set(xlabel = 'frequency [Hz]', ylabel = 'Acceleration')
axs[1, 1].cla()
axs[1, 1].set_title('Position shift vs. Time')

axs[1, 1].plot(t,dis, 'g-',label='', alpha = 0.75)
axs[1, 1].legend()
axs[1, 1].grid()
axs[1, 1].set(xlabel = 'Time [s]', ylabel = 'Position shift[\u03BCm]')





fig.savefig(plot_name + '.png')
fig.show()




