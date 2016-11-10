import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12]


#Creating the list. Logorithm of sample size. Will be plotted in x-axist_0 = [10.000000,12.000000,13.000000,15.375000,15.062500,14.812500,14.562500,22.007812]
t_1 = [26.000000,29.000000,37.750000,28.000000,12.750000,12.843750,12.625000,11.296875]
t_2 = [14.000000,18.500000,12.250000,8.125000,17.875000,16.718750,16.734375,19.695312]
t_3 = [12.000000,18.500000,35.250000,21.875000,21.312500,22.875000,25.500000,35.929688]
t_4 = [13.000000,19.500000,13.250000,14.500000,13.500000,23.625000,36.562500,39.148438]
t_5 = [8.000000,8.500000,23.250000,15.500000,20.625000,21.187500,21.781250,24.390625]
t_6 = [15.000000,21.500000,23.250000,20.000000,21.375000,25.375000,27.312500,44.773438]
t_7 = [11.000000,19.500000,21.500000,32.250000,40.187500,32.875000,28.234375,32.648438]
t_8 = [9.000000,21.500000,15.250000,12.375000,10.312500,17.625000,17.296875,24.156250]
t_9 = [20.000000,23.500000,27.000000,20.125000,13.500000,15.156250,19.718750,29.328125]
t_10 = [10.000000,11.500000,15.000000,15.875000,11.937500,12.250000,16.687500,40.921875]
t_11 = [12.000000,14.000000,13.000000,26.250000,26.062500,36.812500,31.671875,39.742188]
t_12 = [15.000000,9.500000,14.250000,17.750000,20.375000,17.031250,14.281250,29.726562]
t_13 = [22.000000,18.000000,15.500000,10.750000,8.312500,11.343750,16.953125,26.164062]
t_14 = [21.000000,16.000000,12.750000,9.625000,8.500000,14.468750,11.421875,12.460938]
t_15 = [17.000000,15.500000,17.500000,19.500000,21.937500,16.750000,20.984375,16.210938]



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
plt.title('$T(\phi,a)$ in SMALLPRESENT-4 with all zero key upto 27 rounds')
plt.text(5.2,78,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(5.2,85,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(5.2,99,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([5, 12, 0, 120])
plt.grid(True)
plt.show()
