import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12]


#Creating the list. Logorithm of sample size. Will be plotted in x-axist_0 = [16.000000,21.000000,20.750000,16.500000,11.937500,19.093750,18.078125,18.601562]
t_1 = [15.000000,15.000000,8.250000,10.125000,12.750000,11.218750,12.046875,10.343750]
t_2 = [12.000000,9.500000,17.250000,10.000000,2.937500,10.406250,19.515625,23.664062]
t_3 = [14.000000,21.000000,26.000000,18.125000,18.812500,13.281250,14.687500,26.656250]
t_4 = [13.000000,13.500000,12.750000,10.625000,14.500000,16.062500,20.328125,23.710938]
t_5 = [18.000000,14.500000,11.500000,14.000000,12.812500,20.437500,20.921875,17.500000]
t_6 = [9.000000,25.000000,15.500000,15.625000,13.562500,15.875000,23.703125,13.937500]
t_7 = [15.000000,15.000000,16.000000,11.500000,11.125000,13.375000,8.843750,10.968750]
t_8 = [12.000000,10.000000,9.000000,12.125000,6.687500,15.437500,13.796875,16.085938]
t_9 = [12.000000,8.000000,14.750000,18.000000,11.812500,7.968750,9.984375,30.984375]
t_10 = [10.000000,13.000000,13.750000,14.125000,16.187500,20.375000,20.562500,25.640625]
t_11 = [31.000000,26.500000,23.250000,11.500000,20.187500,23.562500,15.078125,11.593750]
t_12 = [21.000000,24.500000,15.000000,20.500000,19.125000,16.812500,15.203125,21.570312]
t_13 = [33.000000,18.500000,23.250000,20.750000,12.187500,14.187500,18.437500,24.031250]
t_14 = [12.000000,10.000000,11.250000,14.250000,13.187500,7.531250,5.609375,6.562500]
t_15 = [22.000000,17.000000,16.250000,18.625000,10.500000,13.125000,19.562500,23.585938]



#Below are the theoretical mean and variances of T for different sample sizes

# sample sizeL 32
mu_32 = 15*(1-32/4096) + 32*0.0046606063
sigma_32 = math.sqrt((2.0/15)*(15*(1-32/4096)+32*0.0046606063)**2)


# sample sizeL 64
mu_64 = 15*(1-64/4096) + 64*0.0046606063
sigma_64 = math.sqrt((2.0/15)*(15*(1-64/4096)+64*0.0046606063)**2)


# sample sizeL 128
mu_128 = 15*(1-128/4096) + 128*0.0046606063
sigma_128 = math.sqrt((2.0/15)*(15*(1-128/4096)+128*0.0046606063)**2)


# sample sizeL 256
mu_256 = 15*(1-256/4096) + 256*0.0046606063
sigma_256 = math.sqrt((2.0/15)*(15*(1-256/4096)+256*0.0046606063)**2)


# sample sizeL 512
mu_512 = 15*(1-512/4096) + 512*0.0046606063
sigma_512 = math.sqrt((2.0/15)*(15*(1-512/4096)+512*0.0046606063)**2)


# sample sizeL 1024
mu_1024 = 15*(1-1024/4096) + 1024*0.0046606063
sigma_1024 = math.sqrt((2.0/15)*(15*(1-1024/4096)+1024*0.0046606063)**2)


# sample sizeL 2048
mu_2048 = 15*(1-2048/4096) + 2048*0.0046606063
sigma_2048 = math.sqrt((2.0/15)*(15*(1-2048/4096)+2048*0.0046606063)**2)


# sample sizeL 4096
mu_4096 = 15*(1-4096/4096) + 4096*0.0046606063
sigma_4096 = math.sqrt((2.0/15)*(15*(1-4096/4096)+4096*0.0046606063)**2)


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
plt.title('$T(\phi,a)$ in SMALLPRESENT-4 with all zero key upto 5 rounds')
plt.text(5.2,78,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(5.2,85,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(5.2,99,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([5, 12, 0, 120])
plt.grid(True)
plt.show()
