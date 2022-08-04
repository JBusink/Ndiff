from matplotlib.axes import Axes
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
from scipy.fft import fft, rfft,rfftfreq


df=pd.read_csv('Munib/Test Slinger Niels Munib.mqa', sep='\t',header=0)



Time = df['Time'].str.replace(',', '.').astype(float).to_list()
Xpos = df['Point #1.X'].str.replace(',', '.').astype(float).to_list()
Ypos = df['Point #1.Y'].str.replace(',', '.').astype(float).to_list()

def model(x,a,b,c,d,e,f,g):
    return a+b*np.sin(c*x+d)+e*np.sin(f*x+g)

# popt, pcov = curve_fit(model,Time,Xpos,p0=[0.3,0.1,4,0,0.0001,0,0])
# fig,axes=plt.subplots(1,1,figsize=(8,3))
# axes.scatter(Time[0::1],Xpos[0::1], color = 'black', s = 15, marker ='+')
# axes.plot(np.linspace(0,5,1001),model(np.linspace(0,5,1001),*popt), color ='darkred', lw = 2)
# axes.set_xlim(0,5)
# axes.set_ylim(0.2,0.5)

# axes.set_xlabel('Time (s)', fontsize=12)
# axes.set_ylabel('X position (m)',fontsize=12)
# axes.tick_params(direction="in")

# # axes.text(1,0.25,r"$f(t) = x_{0} + A(t)\cdot\sin(\omega t+\phi)$", color = 'black', fontsize=12)
# axes.text(1,0.43,"f(t) = " + "{:.2f}".format(popt[0]) +" + "+ "{:.2f}".format(popt[1])
#           +r"sin(" +"{:.2f}".format(popt[2])+ "t"+"{:.2f}".format(popt[3]) + ")"  , color = 'darkred', fontsize=12)
# plt.savefig('Munib/Slinger_xdirection.svg')
# plt.tight_layout()
# plt.show()

# popt, pcov = curve_fit(model,Time,Ypos,p0=[0.485,0.0005,9.2,0,0.001,4.6,0])

# fig,axes=plt.subplots(1,1,figsize=(8,3))
# axes.scatter(Time[0::1],Ypos[0::1], color = 'black', s = 15, marker ='+')
# # axes.plot(np.linspace(0,5,1001),model(np.linspace(0,5,1001),0.487,0.001,9.2,-.90+1.57,0.00,4.64,0), color ='darkred', lw = 2)
# axes.plot(np.linspace(0,5,1001),model(np.linspace(0,5,1001),*popt), color ='darkred', lw = 2)

# axes.set_xlim(0,5)
# axes.set_ylim(0.48,0.5)

# axes.set_xlabel('Time (s)', fontsize=12)
# axes.set_ylabel('y position (m)',fontsize=12)
# axes.tick_params(direction="in")

# # axes.text(1,0.25,r"$f(t) = x_{0} + A(t)\cdot\sin(\omega t+\phi)$", color = 'black', fontsize=12)
# axes.text(0.5,0.495,"f(t) = " + "{:.4f}".format(popt[0]) +" + "+ "{:.3f}".format(popt[1])
#           +r"sin(" +"{:.2f}".format(popt[2])+ "t"+"{:.2f}".format(popt[3]) + ")"  +" + "+ "{:.4f}".format(popt[4])
#           +r"sin(" +"{:.2f}".format(popt[5])+ "t"+"{:.2f}".format(popt[6]) + ")"  , color = 'darkred', fontsize=12)
# plt.savefig('Munib/Slinger_ydirection.svg')
# plt.tight_layout()
# plt.show()
Time = np.asarray(Time)

from scipy.fft import fft, fftfreq
# Number of sample points
A_signal_fft = rfft(np.asarray(Ypos)-np.mean(Ypos))
frequencies = rfftfreq(np.size(Time),1/126.)

fig,axes=plt.subplots(1,1, figsize=(8,4))
axes.plot(frequencies*2*np.pi, np.abs(A_signal_fft), lw=1, c='darkred')
axes.scatter(frequencies*2*np.pi, np.abs(A_signal_fft), s=50, c='black',marker='+')

axes.set_xlim(.1,100)
axes.set_ylim(0.001,10)
axes.set_yscale('log')
axes.set_xscale('log')

axes.set_xlabel("frequency [Hz]",fontsize=12)
axes.set_ylabel(r"$|\mathcal{F}(A_{signal})|$",fontsize=12)
axes.tick_params(direction="in")
plt.savefig('Munib/FFT_Mean_Slinger_Ydirection.svg')
plt.tight_layout()
plt.show()
# print(0.72912146*7,0.72912146*13)