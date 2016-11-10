import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12]


#Creating the list. Logorithm of sample size. Will be plotted in x-axist_0 = [12.000000,20.500000,17.750000,19.375000,17.812500,16.406250,11.046875,8.687500]
t_1 = [18.000000,16.000000,18.250000,13.000000,17.375000,6.593750,18.062500,8.687500]
t_2 = [21.000000,11.500000,7.250000,5.000000,3.937500,17.875000,13.250000,15.710938]
t_3 = [20.000000,15.000000,15.000000,13.000000,8.937500,19.968750,15.000000,17.445312]
t_4 = [14.000000,13.000000,12.250000,16.500000,18.125000,18.500000,14.562500,13.898438]
t_5 = [9.000000,13.500000,19.250000,12.125000,20.062500,14.000000,13.453125,9.468750]
t_6 = [25.000000,22.000000,25.500000,22.500000,10.437500,13.187500,9.406250,16.296875]
t_7 = [12.000000,12.500000,8.000000,14.125000,17.500000,11.062500,6.890625,5.296875]
t_8 = [19.000000,45.500000,34.750000,17.500000,13.937500,10.562500,9.796875,9.625000]
t_9 = [19.000000,15.500000,11.000000,17.625000,16.375000,15.062500,12.218750,13.390625]
t_10 = [8.000000,10.000000,13.000000,9.750000,15.812500,17.031250,17.750000,10.554688]
t_11 = [16.000000,20.000000,25.250000,14.875000,13.562500,7.875000,13.343750,14.109375]
t_12 = [10.000000,16.000000,19.500000,14.625000,25.187500,18.875000,12.921875,8.781250]
t_13 = [23.000000,16.500000,16.000000,11.750000,10.875000,13.625000,14.062500,14.265625]
t_14 = [15.000000,15.000000,13.000000,11.500000,12.062500,18.656250,12.515625,13.937500]
t_15 = [15.000000,13.500000,18.750000,30.250000,15.750000,17.500000,15.000000,14.429688]



#Below are the theoretical mean and variances of T for different sample sizes

# sample sizeL 32
mu_32 = 15*(1-32/4096) + 32*0.0029691457
sigma_32 = math.sqrt((2.0/15)*(15*(1-32/4096)+32*0.0029691457)**2)


# sample sizeL 64
mu_64 = 15*(1-64/4096) + 64*0.0029691457
sigma_64 = math.sqrt((2.0/15)*(15*(1-64/4096)+64*0.0029691457)**2)


# sample sizeL 128
mu_128 = 15*(1-128/4096) + 128*0.0029691457
sigma_128 = math.sqrt((2.0/15)*(15*(1-128/4096)+128*0.0029691457)**2)


# sample sizeL 256
mu_256 = 15*(1-256/4096) + 256*0.0029691457
sigma_256 = math.sqrt((2.0/15)*(15*(1-256/4096)+256*0.0029691457)**2)


# sample sizeL 512
mu_512 = 15*(1-512/4096) + 512*0.0029691457
sigma_512 = math.sqrt((2.0/15)*(15*(1-512/4096)+512*0.0029691457)**2)


# sample sizeL 1024
mu_1024 = 15*(1-1024/4096) + 1024*0.0029691457
sigma_1024 = math.sqrt((2.0/15)*(15*(1-1024/4096)+1024*0.0029691457)**2)


# sample sizeL 2048
mu_2048 = 15*(1-2048/4096) + 2048*0.0029691457
sigma_2048 = math.sqrt((2.0/15)*(15*(1-2048/4096)+2048*0.0029691457)**2)


# sample sizeL 4096
mu_4096 = 15*(1-4096/4096) + 4096*0.0029691457
sigma_4096 = math.sqrt((2.0/15)*(15*(1-4096/4096)+4096*0.0029691457)**2)


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
plt.title('$T(\phi,a)$ in SMALLPRESENT-4 with all zero key upto 7 rounds')
plt.text(5.2,78,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(5.2,85,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(5.2,99,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([5, 12, 0, 120])
plt.grid(True)
plt.show()
