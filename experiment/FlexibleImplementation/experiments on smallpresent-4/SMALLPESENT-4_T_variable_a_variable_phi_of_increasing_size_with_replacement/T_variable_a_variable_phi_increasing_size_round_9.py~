import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12]


#Creating the list. Logorithm of sample size. Will be plotted in x-axist_0 = [13.000000,6.000000,7.000000,9.000000,12.375000,9.968750,7.781250,14.593750]
t_1 = [15.000000,13.000000,18.250000,21.625000,12.750000,23.968750,23.984375,54.390625]
t_2 = [8.000000,9.500000,14.000000,15.750000,21.875000,14.250000,14.359375,12.234375]
t_3 = [9.000000,14.000000,13.500000,14.125000,12.375000,13.656250,24.234375,39.632812]
t_4 = [20.000000,13.000000,11.000000,15.250000,9.375000,16.093750,18.093750,15.609375]
t_5 = [19.000000,26.000000,28.000000,18.625000,18.750000,31.718750,24.296875,38.281250]
t_6 = [15.000000,22.500000,25.250000,23.375000,39.062500,24.093750,29.812500,34.750000]
t_7 = [5.000000,5.000000,7.250000,12.750000,9.062500,8.625000,16.515625,43.664062]
t_8 = [12.000000,15.500000,29.500000,28.250000,29.187500,28.281250,25.765625,34.671875]
t_9 = [16.000000,10.000000,9.750000,6.625000,8.375000,14.687500,17.281250,33.960938]
t_10 = [11.000000,11.500000,20.750000,13.875000,7.062500,21.750000,16.703125,25.828125]
t_11 = [29.000000,12.500000,9.750000,11.875000,17.437500,27.156250,33.156250,44.562500]
t_12 = [6.000000,8.000000,7.000000,14.000000,18.875000,13.562500,16.312500,25.414062]
t_13 = [12.000000,16.500000,10.000000,5.000000,18.437500,10.093750,27.078125,25.234375]
t_14 = [15.000000,13.000000,17.500000,17.125000,19.187500,14.500000,17.828125,26.781250]
t_15 = [23.000000,20.500000,16.750000,6.875000,16.625000,31.250000,37.031250,56.445312]



#Below are the theoretical mean and variances of T for different sample sizes

# sample sizeL 32
mu_32 = 15 + 32*.0041134357
sigma_32 = math.sqrt((2.0/15)*(15+32*.0041134357)**2)


# sample sizeL 64
mu_64 = 15 + 64*.0041134357
sigma_64 = math.sqrt((2.0/15)*(15+64*.0041134357)**2)


# sample sizeL 128
mu_128 = 15 + 128*.0041134357
sigma_128 = math.sqrt((2.0/15)*(15+128*.0041134357)**2)


# sample sizeL 256
mu_256 = 15 + 256*.0041134357
sigma_256 = math.sqrt((2.0/15)*(15+256*.0041134357)**2)


# sample sizeL 512
mu_512 = 15 + 512*.0041134357
sigma_512 = math.sqrt((2.0/15)*(15+512*.0041134357)**2)


# sample sizeL 1024
mu_1024 = 15 + 1024*.0041134357
sigma_1024 = math.sqrt((2.0/15)*(15+1024*.0041134357)**2)


# sample sizeL 2048
mu_2048 = 15 + 2048*.0041134357
sigma_2048 = math.sqrt((2.0/15)*(15+2048*.0041134357)**2)


# sample sizeL 4096
mu_4096 = 15 + 4096*.0041134357
sigma_4096 = math.sqrt((2.0/15)*(15+4096*.0041134357)**2)


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
