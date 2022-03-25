#sample code for scipy
from matplotlib import pyplot as plt
from scipy.integrate import odeint
import numpy as np

#given parameters
k = 50 
m = 50
b = 8
K = k/m
lam = b/m
g = 10

def shm(u,t):
    x = u[0]
    y = u[1]
    dxdt = y
    dydt = -K*x - lam*y + g + 10*k/m
    return np.array([dxdt,dydt])

u0 = [10,10]
t = np.linspace(0,200,1000)

sol = odeint(shm,u0,t)
x = sol[:,0]
y = sol[:,1]

plt.plot(t,x)
#plt.axis([0,20,-1,1])
plt.axhline(lw = 0.5)
plt.show()