import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12]


#Creating the list. Logorithm of sample size. Will be plotted in x-axist_0 = [28.000000,35.000000,28.000000,33.875000,21.937500,26.468750,25.031250,35.648438]
t_1 = [12.000000,19.000000,14.750000,8.750000,16.562500,13.281250,16.484375,18.062500]
t_2 = [14.000000,25.000000,15.500000,12.875000,17.937500,16.437500,35.109375,47.937500]
t_3 = [19.000000,17.000000,13.250000,9.250000,5.687500,10.468750,10.140625,16.125000]
t_4 = [14.000000,17.000000,22.000000,14.500000,14.437500,17.500000,30.625000,26.507812]
t_5 = [20.000000,18.500000,13.000000,14.750000,12.500000,14.656250,16.312500,18.742188]
t_6 = [9.000000,11.000000,9.500000,11.500000,13.250000,13.593750,17.250000,12.804688]
t_7 = [19.000000,19.000000,21.000000,23.375000,16.625000,25.250000,19.750000,30.593750]
t_8 = [12.000000,15.500000,18.250000,11.500000,14.437500,15.656250,12.125000,37.070312]
t_9 = [11.000000,17.500000,14.750000,13.125000,14.125000,25.125000,21.453125,36.164062]
t_10 = [12.000000,15.000000,26.250000,22.750000,22.125000,32.937500,46.109375,42.765625]
t_11 = [14.000000,12.000000,8.750000,7.000000,16.812500,13.937500,14.890625,24.687500]
t_12 = [9.000000,12.500000,9.500000,12.125000,18.875000,16.312500,20.734375,44.218750]
t_13 = [16.000000,20.500000,21.000000,15.500000,10.000000,13.531250,17.359375,34.312500]
t_14 = [9.000000,11.000000,14.500000,11.625000,12.500000,16.906250,12.578125,16.437500]
t_15 = [8.000000,12.500000,12.250000,6.125000,6.500000,12.718750,18.203125,19.625000]



#Below are the theoretical mean and variances of T for different sample sizes

# sample sizeL 32
mu_32 = 15 + 32*xxxx
sigma_32 = math.sqrt((2.0/15)*(15+32*xxxx)**2)


# sample sizeL 64
mu_64 = 15 + 64*xxxx
sigma_64 = math.sqrt((2.0/15)*(15+64*xxxx)**2)


# sample sizeL 128
mu_128 = 15 + 128*xxxx
sigma_128 = math.sqrt((2.0/15)*(15+128*xxxx)**2)


# sample sizeL 256
mu_256 = 15 + 256*xxxx
sigma_256 = math.sqrt((2.0/15)*(15+256*xxxx)**2)


# sample sizeL 512
mu_512 = 15 + 512*xxxx
sigma_512 = math.sqrt((2.0/15)*(15+512*xxxx)**2)


# sample sizeL 1024
mu_1024 = 15 + 1024*xxxx
sigma_1024 = math.sqrt((2.0/15)*(15+1024*xxxx)**2)


# sample sizeL 2048
mu_2048 = 15 + 2048*xxxx
sigma_2048 = math.sqrt((2.0/15)*(15+2048*xxxx)**2)


# sample sizeL 4096
mu_4096 = 15 + 4096*xxxx
sigma_4096 = math.sqrt((2.0/15)*(15+4096*xxxx)**2)


#Plotting 5 different lines to present the theoretical distirbution of T

expected_T_a_0 = []
expected_T_a_0.append(mu_32)
expected_T_a_0.append(mu_64)
expected_T_a_0.append(mu_128)
expected_T_a_0.append(mu_256)
expected_T_a_0.append(mu_512)
expected_T_a_0.append(mu_1024)
expected_T_a_0.append(mu_2048)
expected_T_a_0.append(mu_4096)
plt.plot(t,expected_T_a_0,linewidth=.1, linestyle="-", c="DimGray")

expected_T_a_1 = []
expected_T_a_1.append(mu_32+sigma_32)
expected_T_a_1.append(mu_64+sigma_64)
expected_T_a_1.append(mu_128+sigma_128)
expected_T_a_1.append(mu_256+sigma_256)
expected_T_a_1.append(mu_512+sigma_512)
expected_T_a_1.append(mu_1024+sigma_1024)
expected_T_a_1.append(mu_2048+sigma_2048)
expected_T_a_1.append(mu_4096+sigma_4096)
plt.plot(t,expected_T_a_1,linewidth=.1, linestyle="-", c="DimGray")

expected_T_a_2 = []
expected_T_a_2.append(mu_32-sigma_32)
expected_T_a_2.append(mu_64-sigma_64)
expected_T_a_2.append(mu_128-sigma_128)
expected_T_a_2.append(mu_256-sigma_256)
expected_T_a_2.append(mu_512-sigma_512)
expected_T_a_2.append(mu_1024-sigma_1024)
expected_T_a_2.append(mu_2048-sigma_2048)
expected_T_a_2.append(mu_4096-sigma_4096)
plt.plot(t,expected_T_a_2,linewidth=.1, linestyle="-", c="DimGray")

expected_T_a_3 = []
expected_T_a_3.append(mu_32+2*sigma_32)
expected_T_a_3.append(mu_64+2*sigma_64)
expected_T_a_3.append(mu_128+2*sigma_128)
expected_T_a_3.append(mu_256+2*sigma_256)
expected_T_a_3.append(mu_512+2*sigma_512)
expected_T_a_3.append(mu_1024+2*sigma_1024)
expected_T_a_3.append(mu_2048+2*sigma_2048)
expected_T_a_3.append(mu_4096+2*sigma_4096)
plt.plot(t,expected_T_a_3,linewidth=.1, linestyle="-", c="DimGray")

expected_T_a_4 = []
expected_T_a_4.append(mu_32-2*sigma_32)
expected_T_a_4.append(mu_64-2*sigma_64)
expected_T_a_4.append(mu_128-2*sigma_128)
expected_T_a_4.append(mu_256-2*sigma_256)
expected_T_a_4.append(mu_512-2*sigma_512)
expected_T_a_4.append(mu_1024-2*sigma_1024)
expected_T_a_4.append(mu_2048-2*sigma_2048)
expected_T_a_4.append(mu_4096-2*sigma_4096)
plt.plot(t,expected_T_a_4,linewidth=.1, linestyle="-", c="DimGray")

#Plotting the experimental linesplt.plot(t, t_0, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_1, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_2, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_3, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_4, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_5, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_6, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_7, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_8, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_9, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_10, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_11, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_12, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_13, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_14, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_15, linewidth=.1, linestyle="-", c="red")



#Shading the theoretical distribution region
plt.fill_between(t, expected_T_a_1,expected_T_a_2,color='DimGray',alpha=.7)
plt.fill_between(t, expected_T_a_1,expected_T_a_3,color='DimGray',alpha=.35)
plt.fill_between(t, expected_T_a_2,expected_T_a_4,color='DimGray',alpha=.35)


#Formatting the plot

plt.ylabel('$T(\phi,a)$')
plt.title('$T(\phi,a)$ in SMALLPRESENT-4 with all zero key upto 15 rounds')
plt.text(5.2,78,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(5.2,85,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(5.2,99,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([5, 12, 0, 120])
plt.grid(True)
plt.show()
