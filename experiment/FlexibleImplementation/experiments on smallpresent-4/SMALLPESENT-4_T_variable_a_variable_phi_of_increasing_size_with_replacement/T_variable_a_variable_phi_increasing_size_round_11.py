import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12]


#Creating the list. Logorithm of sample size. Will be plotted in x-axist_0 = [21.000000,28.000000,21.500000,16.000000,19.187500,22.562500,23.125000,20.617188]
t_1 = [5.000000,12.000000,8.750000,12.000000,13.875000,15.687500,14.593750,31.460938]
t_2 = [9.000000,11.000000,22.750000,18.375000,12.625000,16.812500,19.734375,20.742188]
t_3 = [11.000000,9.500000,8.750000,9.500000,9.812500,7.031250,10.218750,18.804688]
t_4 = [34.000000,27.500000,28.500000,46.500000,21.812500,15.812500,22.859375,30.007812]
t_5 = [12.000000,17.500000,16.500000,28.875000,17.312500,25.093750,14.078125,33.367188]
t_6 = [12.000000,13.000000,8.500000,8.000000,12.500000,13.718750,13.203125,24.140625]
t_7 = [9.000000,15.000000,20.500000,9.875000,11.625000,19.781250,17.625000,30.953125]
t_8 = [19.000000,20.500000,26.500000,24.250000,18.062500,16.875000,20.328125,13.593750]
t_9 = [11.000000,8.000000,8.250000,11.250000,9.937500,23.000000,21.421875,27.046875]
t_10 = [18.000000,19.500000,24.250000,17.375000,14.437500,30.000000,22.421875,20.250000]
t_11 = [11.000000,13.000000,9.500000,8.000000,4.062500,11.343750,21.234375,44.273438]
t_12 = [19.000000,10.500000,14.000000,14.625000,8.625000,11.156250,16.921875,20.039062]
t_13 = [16.000000,14.000000,33.000000,21.375000,15.375000,24.468750,34.781250,34.664062]
t_14 = [21.000000,19.500000,20.500000,19.250000,18.187500,16.156250,13.250000,22.015625]
t_15 = [14.000000,14.000000,14.000000,15.750000,16.437500,14.718750,10.687500,16.507812]



#Below are the theoretical mean and variances of T for different sample sizes

# sample sizeL 32
mu_32 = 15 + 32*0.0030920505
sigma_32 = math.sqrt((2.0/15)*(15+32*0.0030920505)**2)


# sample sizeL 64
mu_64 = 15 + 64*0.0030920505
sigma_64 = math.sqrt((2.0/15)*(15+64*0.0030920505)**2)


# sample sizeL 128
mu_128 = 15 + 128*0.0030920505
sigma_128 = math.sqrt((2.0/15)*(15+128*0.0030920505)**2)


# sample sizeL 256
mu_256 = 15 + 256*0.0030920505
sigma_256 = math.sqrt((2.0/15)*(15+256*0.0030920505)**2)


# sample sizeL 512
mu_512 = 15 + 512*0.0030920505
sigma_512 = math.sqrt((2.0/15)*(15+512*0.0030920505)**2)


# sample sizeL 1024
mu_1024 = 15 + 1024*0.0030920505
sigma_1024 = math.sqrt((2.0/15)*(15+1024*0.0030920505)**2)


# sample sizeL 2048
mu_2048 = 15 + 2048*0.0030920505
sigma_2048 = math.sqrt((2.0/15)*(15+2048*0.0030920505)**2)


# sample sizeL 4096
mu_4096 = 15 + 4096*0.0030920505
sigma_4096 = math.sqrt((2.0/15)*(15+4096*0.0030920505)**2)


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
plt.title('$T(\phi,a)$ in SMALLPRESENT-4 with all zero key upto 11 rounds')
plt.text(5.2,78,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(5.2,85,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(5.2,99,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([5, 12, 0, 120])
plt.grid(True)
plt.show()
