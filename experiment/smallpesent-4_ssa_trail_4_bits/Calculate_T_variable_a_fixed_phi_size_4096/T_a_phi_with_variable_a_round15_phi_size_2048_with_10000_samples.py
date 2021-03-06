import random
import matplotlib.pyplot as plt
import numpy as np

#with open('T_a_phi_result.txt') as f:
    #w, h = [int(x) for x in f.readline().split()] # read first line
    #array = []
    #for line in f: # read rest of lines
    #    array.append(int(x) for x in line.split())

with open('T_a_phi_variable_a_variable_phi_size_2048_round_15.txt') as f:
    array = []
    for line in f:
        data = line.split()
        array.append(float(data[0]))



mu, sigma = 21.885376, 7.99140941
x = mu + sigma * np.random.randn(10000)
print array

# the histogram of the data
n, bins, patches = plt.hist(array, 50, normed=1, facecolor='g', alpha=0.75)
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='b', alpha=0.5)


plt.xlabel('$T(\phi,a)$')
plt.ylabel('Probability')
plt.title('$T(\phi,a)$ for where $a$ is variable and $|\phi|=2048$ using 10000 different samples')
plt.text(10,.075,r'using $15$ rounds of SMALLPRESENT-4 with all zero key')
plt.text(10, .065, r'$\mu=21.885376, \sigma^2=63.862624355$ for the theoretical plot in blue')
plt.axis([0, 60, 0, 0.08])
plt.grid(True)
plt.show()
