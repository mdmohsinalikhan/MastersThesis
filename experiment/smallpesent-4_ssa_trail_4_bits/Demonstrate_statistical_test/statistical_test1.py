import random
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math

mean = 10
variance = 15
sigma = math.sqrt(variance)
x = np.linspace(0,70,500)
plt.plot(x,mlab.normpdf(x,mean,sigma),'r-')

mean1 = 20
variance1 = 20
sigma1 = math.sqrt(variance1)
x1 = np.linspace(0,70,500)
plt.plot(x1,mlab.normpdf(x1,mean1,sigma1),'b-')

plt.plot([10,10],[0,0.1],'g--')
plt.plot([20,20],[0,0.09],'g--')

plt.plot([10,14],[0.02,0.02],c = "green", linewidth = 2)
plt.plot([14,14],[0,0.06],'y--')


plt.plot([20,14],[0.02,0.02],c = "blue", linewidth = 2)

plt.xlabel('$T$')
plt.ylabel('Probability')
plt.title('Computing $\\tau$')
plt.text(8,.11,r'$T_0 = (\mu_0,\sigma^2_0)$')
plt.text(18,.1,r'$T_1 = (\mu_1,\sigma^2_1)$')
plt.text(13.8,.011,'$\\tau$')
plt.text(11,.022,'$\sigma_0\zeta_0$')
plt.text(17,.022,'$\sigma_1\zeta_1$')
#plt.text(10, .065, r'$\mu=21.873088, \sigma^2=63.790930487$ for the theoretical plot in red line')
plt.axis([0, 35, 0, 0.12])
plt.show()
