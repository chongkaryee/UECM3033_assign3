import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def p(y,t):
    a=1.0
    b=0.2    
    prey=a*(y[0]-(y[0]*y[1]))
    predator=b*(-y[1]+(y[0]*y[1]))
    pp=[prey,predator]
    return pp

#integrate from 0 to 5 for y0(0) = 0.1, and y1(0) = 1.0
y=np.array([0.1,1.0])
t=np.linspace(0,5,1000) 
ans=sp.integrate.odeint(p,y,t)

#Plot the graphs of y0 and y1 against t
plt.plot(t,ans)
plt.plot(t, ans[:,0], label='prey', color="red")
plt.plot(t, ans[:,1], label='predator', color="green")
plt.axis([0,5,0,1])
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('y0 and y1 against t (1)')
plt.grid(True)
plt.legend(loc='best')
plt.show()

#Plot another graph of y1 against y0
plt.plot(ans[:,0], ans[:,1])
plt.axis([0.1,0.5,0.4,1])
plt.xlabel('Prey')
plt.ylabel('Predator')
plt.title('prey vs predator (1)')
plt.grid(True)
plt.legend(loc='best')
plt.show()

#integrate from 0 to 5 for y0(1) = 0.11, and y1(1) = 1.0
y=np.array([0.11,1.0])
t=np.linspace(0,5,1000) 
ans=sp.integrate.odeint(p,y,t)

#Plot the graphs of y0 and y1 against t
plt.plot(t,ans)
plt.plot(t, ans[:,0], label='prey', color="red")
plt.plot(t, ans[:,1], label='predator', color="green")
plt.axis([0,5,0,1])
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('y0 and y1 against t (2)')
plt.grid(True)
plt.legend(loc='best')
plt.show()

#Plot another graph of y1 against y0
plt.plot(ans[:,0], ans[:,1])
plt.axis([0.1,0.5,0.4,1])
plt.xlabel('Prey')
plt.ylabel('Predator')
plt.title('prey vs predator (2)')
plt.grid(True)
plt.legend(loc='best')
plt.show()




