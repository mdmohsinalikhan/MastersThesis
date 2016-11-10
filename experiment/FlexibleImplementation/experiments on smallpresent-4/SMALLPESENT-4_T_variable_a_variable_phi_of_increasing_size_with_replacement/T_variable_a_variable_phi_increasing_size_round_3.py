import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12]


#Creating the list. Logorithm of sample size. Will be plotted in x-axist_0 = [14.000000,13.000000,16.750000,21.125000,20.062500,21.656250,31.015625,56.609375]
t_1 = [15.000000,15.500000,18.750000,27.000000,30.812500,29.062500,49.265625,87.054688]
t_2 = [18.000000,22.000000,24.500000,23.250000,19.687500,28.281250,44.906250,75.257812]
t_3 = [15.000000,8.500000,9.000000,13.500000,24.812500,41.125000,66.750000,114.218750]
t_4 = [18.000000,30.500000,12.250000,18.000000,40.937500,50.218750,96.968750,113.023438]
t_5 = [14.000000,18.500000,30.500000,35.250000,26.375000,65.312500,112.562500,200.148438]
t_6 = [17.000000,20.500000,15.750000,21.500000,34.062500,58.125000,109.515625,140.679688]
t_7 = [15.000000,16.000000,20.750000,15.375000,28.187500,38.031250,48.484375,91.250000]
t_8 = [13.000000,14.500000,16.500000,16.000000,21.125000,32.093750,34.546875,60.203125]
t_9 = [18.000000,13.000000,14.750000,23.500000,37.687500,55.593750,101.062500,168.539062]
t_10 = [21.000000,10.000000,12.250000,22.625000,28.875000,46.093750,89.093750,164.085938]
t_11 = [15.000000,25.000000,22.750000,21.750000,27.437500,62.593750,113.781250,187.156250]
t_12 = [15.000000,23.500000,29.000000,33.250000,37.812500,38.218750,64.484375,88.804688]
t_13 = [29.000000,19.500000,17.000000,15.250000,22.437500,25.125000,44.500000,74.054688]
t_14 = [12.000000,14.000000,11.250000,10.250000,10.687500,32.500000,82.296875,118.437500]
t_15 = [34.000000,23.000000,26.000000,27.125000,49.437500,84.812500,110.437500,161.906250]



#Below are the theoretical mean and variances of T for different sample sizes

# sample sizeL 32
mu_32 = 15 + 32*0.0263200998
sigma_32 = math.sqrt((2.0/15)*(15+32*0.0263200998)**2)


# sample sizeL 64
mu_64 = 15 + 64*0.0263200998
sigma_64 = math.sqrt((2.0/15)*(15+64*0.0263200998)**2)


# sample sizeL 128
mu_128 = 15 + 128*0.0263200998
sigma_128 = math.sqrt((2.0/15)*(15+128*0.0263200998)**2)


# sample sizeL 256
mu_256 = 15 + 256*0.0263200998
sigma_256 = math.sqrt((2.0/15)*(15+256*0.0263200998)**2)


# sample sizeL 512
mu_512 = 15 + 512*0.0263200998
sigma_512 = math.sqrt((2.0/15)*(15+512*0.0263200998)**2)


# sample sizeL 1024
mu_1024 = 15 + 1024*0.0263200998
sigma_1024 = math.sqrt((2.0/15)*(15+1024*0.0263200998)**2)


# sample sizeL 2048
mu_2048 = 15 + 2048*0.0263200998
sigma_2048 = math.sqrt((2.0/15)*(15+2048*0.0263200998)**2)


# sample sizeL 4096
mu_4096 = 15 + 4096*0.0263200998
sigma_4096 = math.sqrt((2.0/15)*(15+4096*0.0263200998)**2)


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
plt.xlabel('$log_2|\phi|$')
plt.title('$T(\phi,a)$ in SMALLPRESENT-[$4$] with all zero key upto 3 rounds')
plt.text(5.2,78,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(5.2,85,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(5.2,99,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([5, 12, 0, 120])
plt.grid(True)
plt.show()
