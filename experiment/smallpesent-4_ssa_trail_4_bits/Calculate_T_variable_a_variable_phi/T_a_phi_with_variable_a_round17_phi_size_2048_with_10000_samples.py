import random
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math

#with open('T_a_phi_result.txt') as f:
    #w, h = [int(x) for x in f.readline().split()] # read first line
    #array = []
    #for line in f: # read rest of lines
    #    array.append(int(x) for x in line.split())

with open('T_a_phi_variable_a_variable_phi_17_round.txt') as f:
    array = []
    for line in f:
        data = line.split()
        array.append(float(data[0]))



mu, sigma = 21.873088, 7.986922467
x = mu + sigma * np.random.randn(10000)
print array

mean = 21.873088
variance = 63.790930487
sigma = math.sqrt(variance)
x = np.linspace(0,70,500)
plt.plot(x,mlab.normpdf(x,mean,sigma),'r-')

# the histogram of the data
n, bins, patches = plt.hist(array, 50, normed=1, facecolor='Dimgray', alpha=0.75)
#n, bins, patches = plt.hist(x, 50, normed=1, facecolor='b', alpha=0.5)


plt.xlabel('$T(\phi,a)$')
plt.ylabel('Probability')
plt.title('$T(\phi,a)$ for where $a$ is variable and $|\phi|=2048$ using 10000 different samples')
plt.text(5,.070,r'using $17$ rounds of SMALLPRESENT-4 with all zero key')
plt.text(5, .065, r'$\mu=21.873088, \sigma^2=63.790930487$ for the theoretical plot in red line')
plt.axis([0, 60, 0, 0.08])
plt.grid(True)
plt.show()
