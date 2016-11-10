import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12]


#Creating the list. Logorithm of sample size. Will be plotted in x-axist_0 = [19.000000,18.500000,17.250000,13.625000,14.562500,26.531250,26.109375,17.476562]
t_1 = [8.000000,6.000000,8.250000,9.625000,17.437500,14.281250,16.625000,16.843750]
t_2 = [20.000000,25.000000,18.000000,24.750000,21.312500,18.562500,15.890625,13.601562]
t_3 = [8.000000,11.000000,11.500000,13.375000,17.062500,21.781250,26.609375,34.968750]
t_4 = [9.000000,8.000000,8.000000,18.875000,35.812500,27.031250,27.437500,29.070312]
t_5 = [22.000000,30.500000,19.750000,21.375000,26.812500,30.625000,35.156250,41.609375]
t_6 = [15.000000,25.000000,22.750000,14.250000,18.875000,19.000000,27.453125,26.078125]
t_7 = [19.000000,19.000000,20.500000,21.625000,15.812500,11.375000,18.171875,34.164062]
t_8 = [13.000000,8.000000,11.000000,9.625000,10.312500,16.343750,11.640625,19.328125]
t_9 = [17.000000,17.500000,21.250000,20.250000,18.500000,18.281250,20.687500,25.601562]
t_10 = [18.000000,20.000000,26.750000,17.375000,10.375000,13.312500,19.890625,23.031250]
t_11 = [11.000000,8.500000,13.000000,9.500000,15.250000,22.156250,20.953125,30.820312]
t_12 = [15.000000,15.000000,14.500000,14.875000,14.750000,15.906250,17.500000,32.906250]
t_13 = [22.000000,19.500000,24.000000,16.000000,3.437500,8.093750,14.781250,9.554688]
t_14 = [13.000000,11.000000,17.000000,18.000000,13.000000,24.062500,28.453125,34.656250]
t_15 = [18.000000,15.500000,16.500000,13.500000,23.875000,44.562500,34.359375,48.750000]



#Below are the theoretical mean and variances of T for different sample sizes

# sample sizeL 32
mu_32 = 15 + 32*0.0029462575
sigma_32 = math.sqrt((2.0/15)*(15+32*0.0029462575)**2)


# sample sizeL 64
mu_64 = 15 + 64*0.0029462575
sigma_64 = math.sqrt((2.0/15)*(15+64*0.0029462575)**2)


# sample sizeL 128
mu_128 = 15 + 128*0.0029462575
sigma_128 = math.sqrt((2.0/15)*(15+128*0.0029462575)**2)


# sample sizeL 256
mu_256 = 15 + 256*0.0029462575
sigma_256 = math.sqrt((2.0/15)*(15+256*0.0029462575)**2)


# sample sizeL 512
mu_512 = 15 + 512*0.0029462575
sigma_512 = math.sqrt((2.0/15)*(15+512*0.0029462575)**2)


# sample sizeL 1024
mu_1024 = 15 + 1024*0.0029462575
sigma_1024 = math.sqrt((2.0/15)*(15+1024*0.0029462575)**2)


# sample sizeL 2048
mu_2048 = 15 + 2048*0.0029462575
sigma_2048 = math.sqrt((2.0/15)*(15+2048*0.0029462575)**2)


# sample sizeL 4096
mu_4096 = 15 + 4096*0.0029462575
sigma_4096 = math.sqrt((2.0/15)*(15+4096*0.0029462575)**2)


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
plt.title('$T(\phi,a)$ in SMALLPRESENT-4 with all zero key upto 10 rounds')
plt.text(5.2,78,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(5.2,85,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(5.2,99,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([5, 12, 0, 120])
plt.grid(True)
plt.show()
