import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12]


#Creating the list. Logorithm of sample size. Will be plotted in x-axist_0 = [18.000000,22.500000,19.750000,17.125000,22.812500,18.468750,14.296875,8.234375]
t_1 = [12.000000,13.500000,18.000000,10.500000,11.625000,14.218750,9.937500,22.359375]
t_2 = [13.000000,13.500000,18.250000,17.250000,8.562500,7.718750,7.546875,8.960938]
t_3 = [7.000000,12.000000,18.000000,20.250000,11.375000,11.625000,15.609375,19.757812]
t_4 = [5.000000,14.000000,10.500000,11.625000,11.437500,14.000000,24.359375,15.726562]
t_5 = [23.000000,17.500000,19.000000,23.500000,15.562500,18.562500,9.750000,10.710938]
t_6 = [35.000000,15.500000,14.750000,18.875000,14.000000,18.750000,19.375000,23.039062]
t_7 = [14.000000,11.500000,15.250000,9.625000,13.562500,16.031250,14.796875,20.960938]
t_8 = [17.000000,6.000000,9.750000,10.125000,15.375000,10.718750,14.953125,17.500000]
t_9 = [14.000000,14.500000,21.500000,13.125000,22.875000,12.468750,18.593750,9.718750]
t_10 = [18.000000,11.000000,14.000000,14.875000,27.062500,25.031250,19.015625,22.375000]
t_11 = [18.000000,10.000000,16.750000,22.125000,20.375000,37.531250,33.437500,30.968750]
t_12 = [20.000000,16.000000,11.000000,21.375000,17.437500,18.062500,16.953125,13.210938]
t_13 = [17.000000,13.500000,12.000000,15.625000,13.562500,10.250000,13.250000,8.664062]
t_14 = [17.000000,20.500000,14.250000,7.250000,10.312500,10.031250,8.203125,13.937500]
t_15 = [21.000000,16.500000,22.000000,15.875000,15.312500,11.937500,13.156250,23.453125]



#Below are the theoretical mean and variances of T for different sample sizes

# sample sizeL 32
mu_32 = 15*(1-32/4096) + 32*0.0041134357
sigma_32 = math.sqrt((2.0/15)*(15*(1-32/4096)+32*0.0041134357)**2)


# sample sizeL 64
mu_64 = 15*(1-64/4096) + 64*0.0041134357
sigma_64 = math.sqrt((2.0/15)*(15*(1-64/4096)+64*0.0041134357)**2)


# sample sizeL 128
mu_128 = 15*(1-128/4096) + 128*0.0041134357
sigma_128 = math.sqrt((2.0/15)*(15*(1-128/4096)+128*0.0041134357)**2)


# sample sizeL 256
mu_256 = 15*(1-256/4096) + 256*0.0041134357
sigma_256 = math.sqrt((2.0/15)*(15*(1-256/4096)+256*0.0041134357)**2)


# sample sizeL 512
mu_512 = 15*(1-512/4096) + 512*0.0041134357
sigma_512 = math.sqrt((2.0/15)*(15*(1-512/4096)+512*0.0041134357)**2)


# sample sizeL 1024
mu_1024 = 15*(1-1024/4096) + 1024*0.0041134357
sigma_1024 = math.sqrt((2.0/15)*(15*(1-1024/4096)+1024*0.0041134357)**2)


# sample sizeL 2048
mu_2048 = 15*(1-2048/4096) + 2048*0.0041134357
sigma_2048 = math.sqrt((2.0/15)*(15*(1-2048/4096)+2048*0.0041134357)**2)


# sample sizeL 4096
mu_4096 = 15*(1-4096/4096) + 4096*0.0041134357
sigma_4096 = math.sqrt((2.0/15)*(15*(1-4096/4096)+4096*0.0041134357)**2)


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
plt.xlabel('$log_2(|\phi|)$')
plt.title('$T(\phi,a)$ in SMALLPRESENT-4 with all zero key upto 9 rounds')
plt.text(5.2,78,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(5.2,85,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(5.2,99,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([5, 12, 0, 120])
plt.grid(True)
plt.show()
