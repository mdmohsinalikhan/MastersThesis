import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12]


#Creating the list. Logorithm of sample size. Will be plotted in x-axist_0 = [6.000000,6.000000,8.250000,17.375000,11.125000,9.562500,8.500000,6.554688]
t_1 = [15.000000,8.500000,3.250000,11.375000,10.500000,15.468750,21.796875,39.585938]
t_2 = [13.000000,24.500000,21.750000,10.500000,9.562500,10.031250,21.578125,33.359375]
t_3 = [22.000000,19.500000,21.500000,31.250000,24.812500,21.187500,27.203125,46.664062]
t_4 = [10.000000,14.500000,16.500000,18.500000,17.062500,26.656250,21.156250,42.109375]
t_5 = [10.000000,12.500000,17.750000,17.000000,9.500000,19.312500,27.640625,57.328125]
t_6 = [18.000000,20.000000,15.750000,20.875000,19.250000,18.187500,34.953125,49.687500]
t_7 = [22.000000,12.000000,13.750000,22.500000,20.062500,23.406250,23.437500,29.515625]
t_8 = [11.000000,12.000000,22.500000,17.750000,14.375000,18.781250,30.375000,35.531250]
t_9 = [17.000000,15.000000,8.000000,14.250000,12.812500,15.468750,32.250000,58.484375]
t_10 = [24.000000,11.000000,9.500000,14.875000,21.250000,25.281250,22.812500,43.617188]
t_11 = [14.000000,15.000000,11.000000,13.875000,21.750000,22.562500,24.937500,28.023438]
t_12 = [19.000000,19.500000,10.750000,17.625000,11.312500,10.812500,14.328125,19.359375]
t_13 = [19.000000,19.000000,13.750000,16.125000,6.687500,12.937500,17.328125,16.117188]
t_14 = [32.000000,25.000000,15.500000,18.000000,15.625000,16.625000,17.609375,30.437500]
t_15 = [16.000000,11.500000,9.500000,7.625000,14.062500,8.343750,12.281250,18.937500]



#Below are the theoretical mean and variances of T for different sample sizes

# sample sizeL 32
mu_32 = 15*(1-32/4096) + 32*0.0084733963
sigma_32 = math.sqrt((2.0/15)*(15*(1-32/4096)+32*0.0084733963)**2)


# sample sizeL 64
mu_64 = 15*(1-64/4096) + 64*0.0084733963
sigma_64 = math.sqrt((2.0/15)*(15*(1-64/4096)+64*0.0084733963)**2)


# sample sizeL 128
mu_128 = 15*(1-128/4096) + 128*0.0084733963
sigma_128 = math.sqrt((2.0/15)*(15*(1-128/4096)+128*0.0084733963)**2)


# sample sizeL 256
mu_256 = 15*(1-256/4096) + 256*0.0084733963
sigma_256 = math.sqrt((2.0/15)*(15*(1-256/4096)+256*0.0084733963)**2)


# sample sizeL 512
mu_512 = 15*(1-512/4096) + 512*0.0084733963
sigma_512 = math.sqrt((2.0/15)*(15*(1-512/4096)+512*0.0084733963)**2)


# sample sizeL 1024
mu_1024 = 15*(1-1024/4096) + 1024*0.0084733963
sigma_1024 = math.sqrt((2.0/15)*(15*(1-1024/4096)+1024*0.0084733963)**2)


# sample sizeL 2048
mu_2048 = 15*(1-2048/4096) + 2048*0.0084733963
sigma_2048 = math.sqrt((2.0/15)*(15*(1-2048/4096)+2048*0.0084733963)**2)


# sample sizeL 4096
mu_4096 = 15*(1-4096/4096) + 4096*0.0084733963
sigma_4096 = math.sqrt((2.0/15)*(15*(1-4096/4096)+4096*0.0084733963)**2)


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
plt.title('$T(\phi,a)$ in SMALLPRESENT-4 with all zero key upto 4 rounds')
plt.text(5.2,78,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(5.2,85,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(5.2,99,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([5, 12, 0, 120])
plt.grid(True)
plt.show()
