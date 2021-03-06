import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12]


#Creating the list. Logorithm of sample size. Will be plotted in x-axist_0 = [22.000000,17.000000,12.750000,9.000000,11.500000,16.406250,29.953125,46.000000]
t_1 = [15.000000,13.000000,11.000000,17.625000,14.000000,13.843750,22.828125,30.671875]
t_2 = [12.000000,22.000000,20.250000,27.625000,31.187500,33.781250,22.984375,29.734375]
t_3 = [11.000000,10.000000,25.000000,13.500000,8.875000,13.562500,15.453125,45.023438]
t_4 = [14.000000,17.500000,13.500000,11.875000,22.375000,23.468750,34.937500,42.750000]
t_5 = [16.000000,15.000000,16.500000,11.125000,17.812500,12.781250,15.296875,14.695312]
t_6 = [22.000000,12.000000,27.750000,14.000000,17.750000,15.562500,17.062500,15.257812]
t_7 = [9.000000,6.500000,6.250000,13.500000,15.937500,12.625000,14.375000,14.164062]
t_8 = [14.000000,15.000000,11.250000,7.875000,6.250000,15.875000,24.500000,49.015625]
t_9 = [13.000000,17.000000,15.250000,21.375000,16.562500,20.906250,35.031250,51.187500]
t_10 = [15.000000,20.500000,6.000000,10.750000,8.875000,11.718750,25.937500,43.132812]
t_11 = [24.000000,20.500000,18.250000,11.375000,13.437500,15.468750,10.328125,17.023438]
t_12 = [18.000000,14.500000,8.750000,10.625000,13.812500,15.281250,26.500000,51.781250]
t_13 = [13.000000,15.500000,30.000000,35.500000,31.125000,13.937500,14.000000,27.695312]
t_14 = [21.000000,12.000000,28.000000,14.750000,28.250000,31.375000,26.625000,48.492188]
t_15 = [16.000000,26.500000,26.000000,15.500000,25.125000,26.656250,30.828125,39.789062]



#Below are the theoretical mean and variances of T for different sample sizes

# sample sizeL 32
mu_32 = 15 + 32*.0039848089
sigma_32 = math.sqrt((2.0/15)*(15+32*.0039848089)**2)


# sample sizeL 64
mu_64 = 15 + 64*.0039848089
sigma_64 = math.sqrt((2.0/15)*(15+64*.0039848089)**2)


# sample sizeL 128
mu_128 = 15 + 128*.0039848089
sigma_128 = math.sqrt((2.0/15)*(15+128*.0039848089)**2)


# sample sizeL 256
mu_256 = 15 + 256*.0039848089
sigma_256 = math.sqrt((2.0/15)*(15+256*.0039848089)**2)


# sample sizeL 512
mu_512 = 15 + 512*.0039848089
sigma_512 = math.sqrt((2.0/15)*(15+512*.0039848089)**2)


# sample sizeL 1024
mu_1024 = 15 + 1024*.0039848089
sigma_1024 = math.sqrt((2.0/15)*(15+1024*.0039848089)**2)


# sample sizeL 2048
mu_2048 = 15 + 2048*.0039848089
sigma_2048 = math.sqrt((2.0/15)*(15+2048*.0039848089)**2)


# sample sizeL 4096
mu_4096 = 15 + 4096*.0039848089
sigma_4096 = math.sqrt((2.0/15)*(15+4096*.0039848089)**2)


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
plt.title('$T(\phi,a)$ in SMALLPRESENT-4 with all zero key upto 6 rounds')
plt.text(5.2,78,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(5.2,85,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(5.2,99,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([5, 12, 0, 120])
plt.grid(True)
plt.show()
