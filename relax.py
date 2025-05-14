"""
The code below was written by https://github.com/DianaNtz and
is an implementation of the Relaxation methods.
"""

#import libraries
import numpy as np
import matplotlib.pyplot as plt
#Finite Difference Derivative second order
def d2x(f,x):
    dx=x[1]-x[0]
    nx=len(x)
    
    Dxx=np.zeros((nx), dtype='double')
   
    for i in range(0,nx):
                 if(i==0):
                     Dxx[0]=(f[2]-2*f[1]+f[0])/(dx**2)
                 if(i==nx-1):
                     Dxx[nx-1]=(f[nx-1]-2*f[nx-1-1]+f[nx-1-2])/(dx**2)
                 if(i!=0 and i!=nx-1):
                     Dxx[i]=(f[i+1]-2*f[i]+f[i-1])/(dx**2)
    return Dxx
