import numpy as np
import matplotlib.pyplot as plt

def acor(x):
    result = np.correlate(x, x, mode='full')
    return result[result.size/2.:]
# generate some data
time = np.arange(0.,2*np.pi,0.01)
y = np.sin(time)

from numpy import *
import numpy as N
import pylab as P



def estimated_autocorrelation(x):
    n = len(x)
    variance = x.var()
    x = x-x.mean()
    r = N.correlate(x, x, mode = 'full')[-n:]
    #assert N.allclose(r, N.array([(x[:n-k]*x[-(n-k):]).sum() for k in range(n)]))
    result = r/(variance*(N.arange(n, 0, -1)))
    return result

P.plot(time,estimated_autocorrelation(y))
P.plot(time,y)

P.xlabel('time (s)')
P.ylabel('autocorrelation')
P.show()