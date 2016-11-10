import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12]


#Creating the list. Logorithm of sample size. Will be plotted in x-axist_0 = [15.000000,14.500000,20.000000,16.500000,18.062500,19.156250,18.703125,17.320312]
t_1 = [15.000000,11.500000,17.000000,24.500000,27.125000,42.562500,38.875000,39.546875]
t_2 = [14.000000,15.000000,19.500000,22.125000,12.312500,11.218750,14.078125,20.148438]
t_3 = [7.000000,10.000000,9.750000,10.750000,13.562500,23.625000,22.828125,47.968750]
t_4 = [13.000000,15.500000,18.750000,15.375000,20.687500,20.125000,15.031250,21.726562]
t_5 = [10.000000,16.000000,10.000000,9.125000,7.562500,14.687500,20.859375,15.890625]
t_6 = [7.000000,10.000000,20.250000,28.125000,25.437500,31.281250,28.546875,25.031250]
t_7 = [12.000000,18.000000,22.000000,18.875000,20.000000,23.437500,23.531250,36.476562]
t_8 = [20.000000,17.000000,17.250000,14.250000,21.187500,23.218750,31.859375,33.757812]
t_9 = [16.000000,12.000000,12.500000,20.125000,17.625000,7.812500,14.156250,16.304688]
t_10 = [11.000000,17.000000,24.250000,18.625000,15.250000,22.687500,40.593750,34.250000]
t_11 = [9.000000,16.000000,15.500000,17.125000,7.812500,16.125000,21.031250,21.710938]
t_12 = [12.000000,10.500000,9.500000,15.625000,20.875000,24.437500,33.562500,48.320312]
t_13 = [30.000000,26.500000,24.000000,22.375000,30.937500,38.187500,33.796875,45.992188]
t_14 = [9.000000,16.000000,14.500000,16.375000,21.562500,17.312500,9.343750,6.414062]
t_15 = [20.000000,23.500000,14.000000,8.375000,14.000000,14.875000,16.531250,18.343750]



#Below are the theoretical mean and variances of T for different sample sizes

# sample sizeL 32
mu_32 = 15 + 32*0.0034888982
sigma_32 = math.sqrt((2.0/15)*(15+32*0.0034888982)**2)


# sample sizeL 64
mu_64 = 15 + 64*0.0034888982
sigma_64 = math.sqrt((2.0/15)*(15+64*0.0034888982)**2)


# sample sizeL 128
mu_128 = 15 + 128*0.0034888982
sigma_128 = math.sqrt((2.0/15)*(15+128*0.0034888982)**2)


# sample sizeL 256
mu_256 = 15 + 256*0.0034888982
sigma_256 = math.sqrt((2.0/15)*(15+256*0.0034888982)**2)


# sample sizeL 512
mu_512 = 15 + 512*0.0034888982
sigma_512 = math.sqrt((2.0/15)*(15+512*0.0034888982)**2)


# sample sizeL 1024
mu_1024 = 15 + 1024*0.0034888982
sigma_1024 = math.sqrt((2.0/15)*(15+1024*0.0034888982)**2)


# sample sizeL 2048
mu_2048 = 15 + 2048*0.0034888982
sigma_2048 = math.sqrt((2.0/15)*(15+2048*0.0034888982)**2)


# sample sizeL 4096
mu_4096 = 15 + 4096*0.0034888982
sigma_4096 = math.sqrt((2.0/15)*(15+4096*0.0034888982)**2)


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
plt.title('$T(\phi,a)$ in SMALLPRESENT-4 with all zero key upto 12 rounds')
plt.text(5.2,78,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(5.2,85,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(5.2,99,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([5, 12, 0, 120])
plt.grid(True)
plt.show()
