import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12]


#Creating the list. Logorithm of sample size. Will be plotted in x-axist_0 = [23.000000,24.500000,25.750000,21.125000,30.625000,36.468750,33.640625,45.968750]
t_1 = [25.000000,25.500000,22.500000,22.250000,10.312500,22.312500,26.515625,27.593750]
t_2 = [15.000000,16.000000,10.750000,10.500000,8.125000,13.250000,23.265625,25.296875]
t_3 = [10.000000,19.500000,22.750000,19.625000,9.375000,14.000000,18.656250,19.164062]
t_4 = [13.000000,26.500000,17.500000,17.625000,17.187500,16.156250,17.765625,27.851562]
t_5 = [12.000000,8.000000,11.000000,10.750000,9.125000,12.343750,17.984375,22.867188]
t_6 = [10.000000,8.500000,10.750000,10.875000,26.062500,20.593750,31.937500,31.804688]
t_7 = [16.000000,21.000000,10.000000,13.750000,25.750000,18.250000,31.468750,40.335938]
t_8 = [14.000000,11.500000,19.750000,10.750000,6.000000,11.031250,19.359375,28.375000]
t_9 = [14.000000,23.500000,20.750000,9.875000,9.312500,13.312500,9.453125,10.078125]
t_10 = [13.000000,20.500000,17.250000,18.125000,14.875000,24.718750,26.984375,33.703125]
t_11 = [18.000000,23.500000,9.250000,6.375000,11.125000,8.968750,18.453125,15.500000]
t_12 = [20.000000,13.500000,11.000000,11.000000,11.937500,25.531250,21.921875,28.703125]
t_13 = [20.000000,23.500000,10.750000,14.000000,10.125000,19.281250,25.343750,33.367188]
t_14 = [16.000000,7.500000,16.750000,16.000000,14.937500,30.843750,24.421875,38.359375]
t_15 = [8.000000,12.500000,21.000000,21.250000,22.125000,13.375000,26.953125,20.625000]



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
plt.title('$T(\phi,a)$ in SMALLPRESENT-4 with all zero key upto 26 rounds')
plt.text(5.2,78,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(5.2,85,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(5.2,99,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([5, 12, 0, 120])
plt.grid(True)
plt.show()
