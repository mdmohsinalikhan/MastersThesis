import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12]


#Creating the list. Logorithm of sample size. Will be plotted in x-axist_0 = [21.000000,15.000000,15.750000,20.500000,15.125000,14.656250,10.953125,10.281250]
t_1 = [23.000000,9.500000,6.000000,10.875000,9.812500,11.062500,7.359375,6.406250]
t_2 = [10.000000,14.000000,12.250000,13.875000,14.250000,10.062500,13.156250,12.796875]
t_3 = [10.000000,11.500000,8.750000,10.750000,12.562500,6.812500,13.796875,5.320312]
t_4 = [14.000000,6.500000,5.750000,10.250000,9.125000,9.062500,10.093750,8.046875]
t_5 = [15.000000,9.000000,7.250000,10.250000,8.625000,9.031250,10.640625,7.789062]
t_6 = [21.000000,20.000000,12.500000,22.125000,13.375000,10.531250,14.640625,17.101562]
t_7 = [11.000000,13.000000,14.000000,12.125000,14.312500,12.281250,12.703125,8.976562]
t_8 = [24.000000,21.500000,17.500000,12.375000,11.562500,14.312500,14.171875,17.539062]
t_9 = [19.000000,7.500000,9.500000,13.500000,8.937500,13.218750,18.703125,10.335938]
t_10 = [8.000000,10.000000,11.500000,11.375000,15.187500,20.281250,11.328125,8.414062]
t_11 = [12.000000,23.500000,24.000000,28.875000,24.625000,15.125000,17.531250,14.765625]
t_12 = [14.000000,9.500000,16.750000,17.250000,19.000000,14.343750,12.828125,14.468750]
t_13 = [7.000000,15.500000,16.250000,19.375000,23.750000,18.218750,7.328125,16.062500]
t_14 = [34.000000,25.500000,25.750000,26.125000,18.937500,20.593750,10.750000,7.570312]
t_15 = [10.000000,18.500000,17.250000,17.125000,10.187500,19.718750,22.296875,9.851562]



#Below are the theoretical mean and variances of T for different sample sizes

# sample sizeL 32
mu_32 = 15*(1-32/4096) + 32*xxxx
sigma_32 = math.sqrt((2.0/15)*(15*(1-32/4096)+32*xxxx)**2)


# sample sizeL 64
mu_64 = 15*(1-64/4096) + 64*xxxx
sigma_64 = math.sqrt((2.0/15)*(15*(1-64/4096)+64*xxxx)**2)


# sample sizeL 128
mu_128 = 15*(1-128/4096) + 128*xxxx
sigma_128 = math.sqrt((2.0/15)*(15*(1-128/4096)+128*xxxx)**2)


# sample sizeL 256
mu_256 = 15*(1-256/4096) + 256*xxxx
sigma_256 = math.sqrt((2.0/15)*(15*(1-256/4096)+256*xxxx)**2)


# sample sizeL 512
mu_512 = 15*(1-512/4096) + 512*xxxx
sigma_512 = math.sqrt((2.0/15)*(15*(1-512/4096)+512*xxxx)**2)


# sample sizeL 1024
mu_1024 = 15*(1-1024/4096) + 1024*xxxx
sigma_1024 = math.sqrt((2.0/15)*(15*(1-1024/4096)+1024*xxxx)**2)


# sample sizeL 2048
mu_2048 = 15*(1-2048/4096) + 2048*xxxx
sigma_2048 = math.sqrt((2.0/15)*(15*(1-2048/4096)+2048*xxxx)**2)


# sample sizeL 4096
mu_4096 = 15*(1-4096/4096) + 4096*xxxx
sigma_4096 = math.sqrt((2.0/15)*(15*(1-4096/4096)+4096*xxxx)**2)


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
plt.title('$T(\phi,a)$ in SMALLPRESENT-4 with all zero key upto 24 rounds')
plt.text(5.2,78,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(5.2,85,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(5.2,99,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([5, 12, 0, 120])
plt.grid(True)
plt.show()
