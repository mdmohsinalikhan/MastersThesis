import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12]


#Creating the list. Logorithm of sample size. Will be plotted in x-axist_0 = [14.000000,11.500000,11.750000,8.500000,12.000000,14.062500,7.406250,10.492188]
t_1 = [19.000000,20.500000,15.750000,17.000000,15.125000,19.531250,17.953125,13.851562]
t_2 = [10.000000,9.000000,5.500000,7.250000,5.812500,15.812500,24.234375,20.601562]
t_3 = [25.000000,21.000000,14.250000,7.000000,10.812500,10.437500,16.468750,9.882812]
t_4 = [14.000000,9.500000,16.250000,25.625000,27.750000,16.906250,20.671875,14.015625]
t_5 = [7.000000,14.000000,14.500000,19.875000,16.812500,16.968750,21.640625,21.328125]
t_6 = [13.000000,15.000000,17.000000,26.500000,18.000000,11.968750,22.109375,29.531250]
t_7 = [16.000000,10.000000,10.250000,6.875000,11.437500,13.531250,11.328125,18.453125]
t_8 = [15.000000,11.000000,17.250000,23.250000,15.750000,11.593750,12.875000,9.296875]
t_9 = [18.000000,14.500000,12.500000,12.500000,7.625000,11.187500,12.000000,4.945312]
t_10 = [11.000000,15.500000,16.250000,6.250000,11.750000,6.000000,17.250000,11.328125]
t_11 = [23.000000,16.000000,20.750000,13.500000,11.812500,12.343750,14.093750,9.585938]
t_12 = [22.000000,17.500000,21.000000,21.625000,16.187500,12.562500,13.312500,20.953125]
t_13 = [18.000000,19.500000,19.750000,13.500000,10.500000,12.000000,11.234375,18.523438]
t_14 = [5.000000,12.000000,12.000000,8.000000,9.562500,14.531250,15.468750,21.664062]
t_15 = [15.000000,13.500000,15.250000,16.250000,15.937500,10.062500,16.812500,19.445312]



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
plt.title('$T(\phi,a)$ in SMALLPRESENT-8 with all zero key upto 4 rounds')
plt.text(5.2,78,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(5.2,85,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(5.2,99,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([5, 12, 0, 120])
plt.grid(True)
plt.show()
