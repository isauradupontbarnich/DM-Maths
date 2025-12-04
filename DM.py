<<<<<<< HEAD


=======
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
    time=[t0+i*dt for i in range(np.floor(tf-t0))]
    for i in range(len(time)-1):
        sol.append(sol[-1]+dt*f(sol[-1],time[i]))

    return time, sol


 
>>>>>>> e12bd8dff1132668205a70a3b84772e9f7ec7ec1
