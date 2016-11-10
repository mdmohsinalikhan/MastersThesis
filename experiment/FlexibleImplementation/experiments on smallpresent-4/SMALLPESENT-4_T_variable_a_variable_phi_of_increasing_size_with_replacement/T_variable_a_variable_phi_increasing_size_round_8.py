import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12]


#Creating the list. Logorithm of sample size. Will be plotted in x-axist_0 = [7.000000,15.000000,14.500000,19.375000,10.875000,7.562500,17.875000,19.742188]
t_1 = [7.000000,18.000000,22.000000,16.125000,18.875000,13.781250,14.265625,19.273438]
t_2 = [16.000000,17.000000,7.750000,6.875000,15.312500,21.531250,12.500000,19.609375]
t_3 = [19.000000,13.000000,12.500000,12.250000,14.750000,15.187500,18.093750,37.242188]
t_4 = [11.000000,13.500000,7.000000,10.000000,18.875000,24.437500,21.078125,29.671875]
t_5 = [17.000000,18.500000,17.250000,17.125000,17.000000,9.468750,13.187500,18.757812]
t_6 = [20.000000,16.500000,23.750000,20.625000,25.937500,17.375000,25.593750,37.906250]
t_7 = [16.000000,14.500000,14.000000,12.750000,13.187500,13.625000,14.312500,29.390625]
t_8 = [14.000000,15.000000,21.500000,21.250000,22.437500,18.500000,23.515625,37.695312]
t_9 = [18.000000,9.500000,9.500000,11.875000,16.312500,14.968750,17.171875,27.445312]
t_10 = [12.000000,13.500000,14.250000,20.250000,15.687500,15.843750,11.765625,24.375000]
t_11 = [14.000000,20.000000,17.500000,24.625000,23.062500,17.906250,26.500000,33.921875]
t_12 = [20.000000,17.000000,15.000000,11.375000,6.812500,7.218750,23.515625,28.148438]
t_13 = [22.000000,5.500000,7.000000,17.375000,17.687500,15.500000,26.000000,37.218750]
t_14 = [21.000000,17.500000,16.500000,11.625000,11.750000,17.687500,23.046875,25.820312]
t_15 = [17.000000,10.000000,6.500000,8.125000,20.937500,22.312500,30.578125,41.234375]



#Below are the theoretical mean and variances of T for different sample sizes

# sample sizeL 32
mu_32 = 15 + 32*.0041698217
sigma_32 = math.sqrt((2.0/15)*(15+32*.0041698217)**2)


# sample sizeL 64
mu_64 = 15 + 64*.0041698217
sigma_64 = math.sqrt((2.0/15)*(15+64*.0041698217)**2)


# sample sizeL 128
mu_128 = 15 + 128*.0041698217
sigma_128 = math.sqrt((2.0/15)*(15+128*.0041698217)**2)


# sample sizeL 256
mu_256 = 15 + 256*.0041698217
sigma_256 = math.sqrt((2.0/15)*(15+256*.0041698217)**2)


# sample sizeL 512
mu_512 = 15 + 512*.0041698217
sigma_512 = math.sqrt((2.0/15)*(15+512*.0041698217)**2)


# sample sizeL 1024
mu_1024 = 15 + 1024*.0041698217
sigma_1024 = math.sqrt((2.0/15)*(15+1024*.0041698217)**2)


# sample sizeL 2048
mu_2048 = 15 + 2048*.0041698217
sigma_2048 = math.sqrt((2.0/15)*(15+2048*.0041698217)**2)


# sample sizeL 4096
mu_4096 = 15 + 4096*.0041698217
sigma_4096 = math.sqrt((2.0/15)*(15+4096*.0041698217)**2)


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
plt.title('$T(\phi,a)$ in SMALLPRESENT-4 with all zero key upto 8 rounds')
plt.text(5.2,78,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(5.2,85,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(5.2,99,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([5, 12, 0, 120])
plt.grid(True)
plt.show()
