import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12]


#Creating the list. Logorithm of sample size. Will be plotted in x-axist_0 = [18.000000,19.000000,17.500000,10.875000,17.000000,13.343750,12.406250,17.195312]
t_1 = [16.000000,14.500000,22.000000,27.125000,18.062500,12.468750,17.468750,17.906250]
t_2 = [25.000000,27.000000,15.250000,21.375000,15.375000,17.593750,11.906250,13.367188]
t_3 = [14.000000,11.500000,17.750000,19.375000,23.875000,24.843750,12.796875,20.398438]
t_4 = [8.000000,8.500000,5.500000,9.125000,10.250000,11.500000,18.218750,32.679688]
t_5 = [8.000000,14.000000,18.000000,16.625000,23.500000,23.531250,22.078125,28.226562]
t_6 = [17.000000,20.000000,16.000000,19.875000,28.500000,20.218750,25.718750,37.226562]
t_7 = [13.000000,12.000000,18.500000,10.500000,21.375000,30.687500,42.312500,53.406250]
t_8 = [5.000000,9.500000,13.750000,12.625000,7.562500,10.125000,12.375000,24.789062]
t_9 = [12.000000,10.500000,8.250000,20.375000,12.500000,14.000000,38.296875,45.359375]
t_10 = [11.000000,16.000000,10.250000,10.000000,11.312500,12.031250,17.562500,19.554688]
t_11 = [14.000000,11.000000,14.500000,16.000000,21.687500,19.156250,29.234375,34.078125]
t_12 = [21.000000,17.000000,17.000000,13.875000,14.062500,21.750000,22.359375,27.804688]
t_13 = [16.000000,16.000000,12.000000,10.375000,11.375000,19.687500,24.515625,32.789062]
t_14 = [13.000000,8.500000,7.000000,10.875000,18.750000,18.875000,24.000000,37.125000]
t_15 = [15.000000,10.500000,7.500000,10.125000,18.250000,25.281250,25.859375,31.429688]



#Below are the theoretical mean and variances of T for different sample sizes

# sample sizeL 32
mu_32 = 15 + 32*xxxx
sigma_32 = math.sqrt((2.0/15)*(15+32*xxxx)**2)


# sample sizeL 64
mu_64 = 15 + 64*xxxx
sigma_64 = math.sqrt((2.0/15)*(15+64*xxxx)**2)


# sample sizeL 128
mu_128 = 15 + 128*xxxx
sigma_128 = math.sqrt((2.0/15)*(15+128*xxxx)**2)


# sample sizeL 256
mu_256 = 15 + 256*xxxx
sigma_256 = math.sqrt((2.0/15)*(15+256*xxxx)**2)


# sample sizeL 512
mu_512 = 15 + 512*xxxx
sigma_512 = math.sqrt((2.0/15)*(15+512*xxxx)**2)


# sample sizeL 1024
mu_1024 = 15 + 1024*xxxx
sigma_1024 = math.sqrt((2.0/15)*(15+1024*xxxx)**2)


# sample sizeL 2048
mu_2048 = 15 + 2048*xxxx
sigma_2048 = math.sqrt((2.0/15)*(15+2048*xxxx)**2)


# sample sizeL 4096
mu_4096 = 15 + 4096*xxxx
sigma_4096 = math.sqrt((2.0/15)*(15+4096*xxxx)**2)


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
plt.title('$T(\phi,a)$ in SMALLPRESENT-4 with all zero key upto 28 rounds')
plt.text(5.2,78,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(5.2,85,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(5.2,99,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([5, 12, 0, 120])
plt.grid(True)
plt.show()
