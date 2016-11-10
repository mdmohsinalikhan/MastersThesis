import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12]


#Creating the list. Logorithm of sample size. Will be plotted in x-axist_0 = [17.000000,11.500000,17.000000,10.625000,17.562500,9.968750,15.843750,14.328125]
t_1 = [13.000000,15.500000,21.500000,14.625000,26.875000,23.843750,26.656250,25.687500]
t_2 = [14.000000,11.000000,9.000000,6.625000,16.812500,22.062500,17.296875,17.585938]
t_3 = [16.000000,17.500000,14.250000,24.250000,22.250000,18.375000,19.531250,24.718750]
t_4 = [10.000000,12.000000,14.250000,5.125000,10.312500,14.562500,11.265625,17.031250]
t_5 = [13.000000,12.000000,11.750000,20.750000,25.062500,27.812500,33.937500,40.015625]
t_6 = [15.000000,20.500000,30.250000,28.500000,28.250000,32.500000,36.562500,38.015625]
t_7 = [6.000000,18.500000,11.500000,17.000000,11.937500,18.406250,14.562500,15.468750]
t_8 = [15.000000,14.000000,16.750000,14.500000,10.312500,9.531250,18.859375,47.789062]
t_9 = [18.000000,10.000000,20.250000,14.750000,6.312500,11.062500,30.171875,37.640625]
t_10 = [23.000000,20.500000,17.250000,26.250000,28.125000,27.750000,29.906250,51.757812]
t_11 = [11.000000,6.000000,14.750000,13.625000,14.312500,14.437500,21.328125,32.351562]
t_12 = [15.000000,12.000000,11.000000,13.750000,9.000000,13.406250,36.156250,37.023438]
t_13 = [8.000000,8.000000,17.000000,14.125000,11.437500,13.468750,18.781250,28.007812]
t_14 = [9.000000,11.000000,17.750000,10.750000,6.125000,12.125000,16.859375,21.375000]
t_15 = [7.000000,7.500000,12.250000,13.625000,14.375000,17.375000,27.625000,59.617188]



#Below are the theoretical mean and variances of T for different sample sizes

# sample sizeL 32
mu_32 = 15 + 32*.0029691457
sigma_32 = math.sqrt((2.0/15)*(15+32*.0029691457)**2)


# sample sizeL 64
mu_64 = 15 + 64*.0029691457
sigma_64 = math.sqrt((2.0/15)*(15+64*.0029691457)**2)


# sample sizeL 128
mu_128 = 15 + 128*.0029691457
sigma_128 = math.sqrt((2.0/15)*(15+128*.0029691457)**2)


# sample sizeL 256
mu_256 = 15 + 256*.0029691457
sigma_256 = math.sqrt((2.0/15)*(15+256*.0029691457)**2)


# sample sizeL 512
mu_512 = 15 + 512*.0029691457
sigma_512 = math.sqrt((2.0/15)*(15+512*.0029691457)**2)


# sample sizeL 1024
mu_1024 = 15 + 1024*.0029691457
sigma_1024 = math.sqrt((2.0/15)*(15+1024*.0029691457)**2)


# sample sizeL 2048
mu_2048 = 15 + 2048*.0029691457
sigma_2048 = math.sqrt((2.0/15)*(15+2048*.0029691457)**2)


# sample sizeL 4096
mu_4096 = 15 + 4096*.0029691457
sigma_4096 = math.sqrt((2.0/15)*(15+4096*.0029691457)**2)


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
