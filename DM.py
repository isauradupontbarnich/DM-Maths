import numpy as np  
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint

#%matplotlib notebook
plt.rcParams["figure.figsize"] = (7,4)
# Dynamique non différentiable (NSD1)
#Question 1:
def euler_explicit (f,x0,t0,tf,dt):
    sol=[x0]
    time=[t0+i*dt for i in range (int(np.floor((tf-t0)//dt)))]
    for i in range(len(time)-1):
        sol.append(sol[-1]+dt*f(sol[-1],time[i]))

    return time, sol

def f(x,t):
    return -np.sqrt(np.abs(x))

time,sol=euler_explicit(f,10,0,10,0.1)
plt.plot(time,sol,'r',label='Euler')

solo=odeint(f,10,time)
plt.plot(time,solo,label='odeint')
plt.legend()
plt.show()
