import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12]


#Creating the list. Logorithm of sample size. Will be plotted in x-axist_0 = [14.000000,14.500000,21.000000,20.500000,16.937500,13.812500,18.625000,33.234375]
t_1 = [16.000000,15.000000,19.250000,16.750000,17.750000,26.718750,31.796875,28.195312]
t_2 = [14.000000,11.500000,9.750000,14.125000,8.187500,19.250000,17.265625,24.554688]
t_3 = [9.000000,15.000000,17.000000,12.500000,14.437500,12.031250,19.531250,24.742188]
t_4 = [16.000000,17.500000,17.000000,15.625000,13.687500,18.218750,26.828125,28.929688]
t_5 = [14.000000,12.500000,10.500000,10.125000,11.062500,14.406250,21.546875,16.882812]
t_6 = [12.000000,10.500000,19.250000,6.750000,11.250000,19.406250,12.312500,35.390625]
t_7 = [16.000000,17.500000,20.250000,19.625000,29.625000,32.343750,33.890625,42.718750]
t_8 = [9.000000,9.500000,12.750000,14.250000,16.000000,20.875000,24.031250,33.203125]
t_9 = [25.000000,17.000000,15.250000,25.250000,20.750000,21.218750,28.375000,55.054688]
t_10 = [14.000000,11.000000,11.000000,11.875000,14.562500,26.250000,26.390625,34.867188]
t_11 = [22.000000,17.000000,24.500000,18.625000,12.750000,11.687500,9.046875,21.351562]
t_12 = [14.000000,14.000000,11.000000,15.250000,8.312500,12.406250,30.484375,54.101562]
t_13 = [12.000000,12.000000,5.750000,9.250000,18.062500,20.781250,44.109375,62.460938]
t_14 = [11.000000,13.500000,13.000000,20.000000,23.562500,26.656250,23.828125,34.656250]
t_15 = [8.000000,8.500000,4.000000,9.625000,10.375000,12.312500,11.406250,21.335938]



#Below are the theoretical mean and variances of T for different sample sizes

# sample sizeL 32
mu_32 = 15 + 32*.0046606063 
sigma_32 = math.sqrt((2.0/15)*(15+32*.0046606063 )**2)


# sample sizeL 64
mu_64 = 15 + 64*.0046606063 
sigma_64 = math.sqrt((2.0/15)*(15+64*.0046606063 )**2)


# sample sizeL 128
mu_128 = 15 + 128*.0046606063 
sigma_128 = math.sqrt((2.0/15)*(15+128*.0046606063 )**2)


# sample sizeL 256
mu_256 = 15 + 256*.0046606063 
sigma_256 = math.sqrt((2.0/15)*(15+256*.0046606063 )**2)


# sample sizeL 512
mu_512 = 15 + 512*.0046606063 
sigma_512 = math.sqrt((2.0/15)*(15+512*.0046606063 )**2)


# sample sizeL 1024
mu_1024 = 15 + 1024*.0046606063 
sigma_1024 = math.sqrt((2.0/15)*(15+1024*.0046606063 )**2)


# sample sizeL 2048
mu_2048 = 15 + 2048*.0046606063 
sigma_2048 = math.sqrt((2.0/15)*(15+2048*.0046606063 )**2)


# sample sizeL 4096
mu_4096 = 15 + 4096*.0046606063 
sigma_4096 = math.sqrt((2.0/15)*(15+4096*.0046606063 )**2)


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
plt.title('$T(\phi,a)$ in SMALLPRESENT-4 with all zero key upto 5 rounds')
plt.text(5.2,78,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(5.2,85,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(5.2,99,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([5, 12, 0, 120])
plt.grid(True)
plt.show()
