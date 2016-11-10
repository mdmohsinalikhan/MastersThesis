import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12]


#Creating the list. Logorithm of sample size. Will be plotted in x-axist_0 = [30.000000,15.500000,19.000000,14.500000,23.437500,14.250000,20.953125,35.390625]
t_1 = [14.000000,9.500000,8.000000,5.000000,14.250000,15.687500,14.515625,19.210938]
t_2 = [13.000000,15.000000,14.750000,15.125000,9.375000,16.593750,19.375000,25.953125]
t_3 = [11.000000,13.500000,17.750000,16.750000,23.187500,28.500000,39.656250,35.031250]
t_4 = [15.000000,14.500000,20.500000,22.250000,13.062500,22.968750,23.765625,23.281250]
t_5 = [10.000000,15.500000,19.000000,18.125000,13.937500,19.656250,23.781250,27.781250]
t_6 = [12.000000,8.500000,20.000000,19.750000,18.000000,14.250000,20.437500,28.648438]
t_7 = [12.000000,13.500000,18.500000,18.125000,12.125000,9.187500,15.578125,16.453125]
t_8 = [12.000000,6.500000,4.750000,10.250000,9.312500,12.625000,14.484375,16.757812]
t_9 = [17.000000,18.500000,20.250000,30.750000,28.625000,32.250000,36.203125,30.929688]
t_10 = [19.000000,14.500000,19.000000,15.000000,9.312500,15.000000,17.421875,30.484375]
t_11 = [13.000000,15.500000,30.250000,21.750000,19.187500,25.656250,32.609375,30.070312]
t_12 = [14.000000,13.000000,15.750000,12.625000,17.750000,21.343750,22.375000,36.085938]
t_13 = [18.000000,18.500000,14.750000,9.250000,30.500000,21.468750,15.468750,20.414062]
t_14 = [11.000000,16.500000,20.250000,20.500000,23.000000,17.718750,13.000000,20.484375]
t_15 = [15.000000,10.000000,16.250000,19.000000,18.312500,29.656250,19.984375,30.742188]



#Below are the theoretical mean and variances of T for different sample sizes

# sample sizeL 32
mu_32 = 15 + 32*0.0029666423
sigma_32 = math.sqrt((2.0/15)*(15+32*0.0029666423)**2)


# sample sizeL 64
mu_64 = 15 + 64*0.0029666423
sigma_64 = math.sqrt((2.0/15)*(15+64*0.0029666423)**2)


# sample sizeL 128
mu_128 = 15 + 128*0.0029666423
sigma_128 = math.sqrt((2.0/15)*(15+128*0.0029666423)**2)


# sample sizeL 256
mu_256 = 15 + 256*0.0029666423
sigma_256 = math.sqrt((2.0/15)*(15+256*0.0029666423)**2)


# sample sizeL 512
mu_512 = 15 + 512*0.0029666423
sigma_512 = math.sqrt((2.0/15)*(15+512*0.0029666423)**2)


# sample sizeL 1024
mu_1024 = 15 + 1024*0.0029666423
sigma_1024 = math.sqrt((2.0/15)*(15+1024*0.0029666423)**2)


# sample sizeL 2048
mu_2048 = 15 + 2048*0.0029666423
sigma_2048 = math.sqrt((2.0/15)*(15+2048*0.0029666423)**2)


# sample sizeL 4096
mu_4096 = 15 + 4096*0.0029666423
sigma_4096 = math.sqrt((2.0/15)*(15+4096*0.0029666423)**2)


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
plt.xlabel('$log_2|\phi|$')
plt.title('$T(\phi,a)$ in SMALLPRESENT-[$4$] with all zero key upto 23 rounds')
plt.text(5.2,78,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(5.2,85,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(5.2,99,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([5, 12, 0, 120])
plt.grid(True)
plt.show()
