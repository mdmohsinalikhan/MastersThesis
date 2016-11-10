import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12]


#Creating the list. Logorithm of sample size. Will be plotted in x-axist_0 = [17.000000,11.000000,19.750000,22.250000,14.562500,14.031250,10.625000,6.398438]
t_1 = [9.000000,13.000000,14.250000,27.375000,16.000000,14.125000,12.828125,14.234375]
t_2 = [17.000000,19.000000,18.500000,20.000000,16.875000,9.562500,10.125000,10.914062]
t_3 = [10.000000,11.500000,13.750000,23.000000,14.062500,10.687500,20.453125,13.039062]
t_4 = [21.000000,15.000000,9.250000,8.750000,8.125000,12.437500,18.718750,16.101562]
t_5 = [14.000000,19.500000,19.250000,16.250000,9.500000,14.250000,20.203125,14.648438]
t_6 = [11.000000,13.500000,12.750000,7.750000,12.875000,12.562500,20.781250,21.875000]
t_7 = [15.000000,14.000000,17.000000,14.375000,10.375000,9.093750,9.671875,7.500000]
t_8 = [11.000000,15.500000,5.750000,13.250000,14.625000,13.843750,11.937500,11.835938]
t_9 = [9.000000,9.000000,8.250000,18.250000,11.125000,18.281250,17.328125,19.320312]
t_10 = [13.000000,9.500000,13.750000,12.125000,11.375000,15.406250,17.109375,11.132812]
t_11 = [19.000000,25.500000,23.750000,14.500000,11.062500,13.750000,20.812500,11.421875]
t_12 = [23.000000,18.000000,18.000000,15.875000,13.500000,17.906250,17.093750,15.203125]
t_13 = [10.000000,11.000000,7.000000,7.500000,8.375000,16.687500,12.265625,16.656250]
t_14 = [15.000000,10.500000,17.250000,12.625000,9.875000,9.812500,13.593750,12.976562]
t_15 = [9.000000,5.000000,5.500000,16.375000,27.500000,21.062500,27.515625,19.070312]



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
plt.title('$T(\phi,a)$ in SMALLPRESENT-11 with all zero key upto 4 rounds')
plt.text(5.2,78,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(5.2,85,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(5.2,99,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([5, 12, 0, 120])
plt.grid(True)
plt.show()
