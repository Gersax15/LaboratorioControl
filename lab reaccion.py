import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dz/dt
def model(z,t):
    K1=100 #L/mol*s
    K2=10 #L/mol*s
    
    F= 264 #L/s
    V= 2132 #L
    
    dCadt = (1/V)*F*(z0[0]-z[0])-K1*z[0]*z[1]
    dCbdt = (1/V)*F*(z0[1]-z[1])-K1*z[0]*z[1]-K2*z[1]*z[2]
    dCrdt = -(1/V)*F*z[2]+K1*z[0]*z[1]-K2*z[1]*z[2]
    dCsdt = -(1/V)*F*z[3]+K2*z[1]*z[2]
    dzdt = [dCadt,dCbdt,dCrdt,dCsdt]
    return dzdt

# initial condition
z0 = [1.25,1.61,0,0]

# time points
t = np.linspace(0,0.8,100)

# solve ODE
z = odeint(model,z0,t)
print(z)


# plot results
plt.plot(t,z[:,0],'b-',label=r'Ca')
plt.plot(t,z[:,1],'g-',label=r'Cb')
plt.plot(t,z[:,2],'r-',label=r'Cr')
plt.plot(t,z[:,3],'c-',label=r'Cs')

plt.ylabel('Concentración (M)')
plt.xlabel('tiempo (s)')
plt.legend(loc='best')
plt.show()