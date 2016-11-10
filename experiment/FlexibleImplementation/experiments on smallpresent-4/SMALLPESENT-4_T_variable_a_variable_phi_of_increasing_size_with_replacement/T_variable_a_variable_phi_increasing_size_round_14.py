import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12]


#Creating the list. Logorithm of sample size. Will be plotted in x-axist_0 = [28.000000,27.000000,26.250000,28.125000,31.500000,35.437500,27.375000,37.562500]
t_1 = [19.000000,27.000000,22.250000,20.625000,10.437500,19.531250,18.375000,12.953125]
t_2 = [13.000000,16.000000,16.000000,13.125000,8.000000,15.906250,11.015625,18.343750]
t_3 = [32.000000,21.000000,16.250000,19.625000,25.000000,23.406250,38.140625,26.593750]
t_4 = [12.000000,15.500000,15.250000,14.125000,21.562500,35.468750,44.234375,46.101562]
t_5 = [15.000000,27.500000,29.750000,16.500000,11.437500,19.843750,15.328125,17.843750]
t_6 = [14.000000,21.500000,16.000000,21.125000,21.375000,20.687500,24.531250,25.929688]
t_7 = [14.000000,13.500000,6.500000,13.125000,16.187500,18.000000,12.500000,34.351562]
t_8 = [11.000000,21.500000,14.500000,26.375000,21.562500,21.937500,15.609375,15.414062]
t_9 = [15.000000,21.000000,13.750000,8.750000,14.500000,14.218750,20.171875,25.945312]
t_10 = [13.000000,14.000000,23.000000,28.875000,38.312500,34.812500,39.453125,59.617188]
t_11 = [6.000000,9.000000,6.750000,10.625000,15.437500,26.187500,27.015625,59.664062]
t_12 = [24.000000,14.500000,9.250000,16.625000,24.812500,18.906250,28.484375,35.507812]
t_13 = [17.000000,28.500000,23.500000,15.500000,9.312500,10.218750,18.718750,9.617188]
t_14 = [19.000000,21.000000,20.000000,21.250000,14.625000,11.906250,17.437500,27.523438]
t_15 = [13.000000,14.000000,11.750000,15.375000,15.062500,15.000000,21.421875,40.882812]



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
plt.title('$T(\phi,a)$ in SMALLPRESENT-4 with all zero key upto 14 rounds')
plt.text(5.2,78,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(5.2,85,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(5.2,99,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([5, 12, 0, 120])
plt.grid(True)
plt.show()
