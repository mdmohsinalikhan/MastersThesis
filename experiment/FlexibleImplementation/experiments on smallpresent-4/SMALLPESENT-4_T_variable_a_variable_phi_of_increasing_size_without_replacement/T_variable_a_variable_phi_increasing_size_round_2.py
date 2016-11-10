import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12]


#Creating the list. Logorithm of sample size. Will be plotted in x-axist_0 = [16.000000,22.500000,20.750000,28.125000,61.812500,119.750000,230.656250,384.000000]
t_1 = [11.000000,14.500000,16.750000,40.750000,55.437500,96.406250,162.953125,324.000000]
t_2 = [12.000000,21.500000,17.750000,29.250000,43.937500,100.437500,150.156250,324.000000]
t_3 = [27.000000,19.000000,27.000000,48.125000,73.375000,117.125000,207.734375,384.000000]
t_4 = [23.000000,32.000000,26.500000,55.375000,79.312500,138.437500,202.218750,324.000000]
t_5 = [26.000000,22.000000,25.250000,37.375000,65.625000,124.625000,196.734375,384.000000]
t_6 = [13.000000,16.000000,22.250000,48.125000,86.062500,122.750000,216.156250,384.000000]
t_7 = [19.000000,18.000000,29.750000,45.875000,68.187500,82.312500,166.906250,324.000000]
t_8 = [13.000000,18.500000,25.500000,36.000000,67.750000,124.375000,213.812500,324.000000]
t_9 = [16.000000,22.500000,21.750000,41.500000,63.250000,105.781250,211.890625,384.000000]
t_10 = [23.000000,18.500000,27.750000,48.875000,70.937500,129.500000,226.390625,384.000000]
t_11 = [27.000000,17.500000,20.250000,40.750000,58.000000,98.968750,174.859375,324.000000]
t_12 = [20.000000,21.500000,28.750000,40.125000,48.500000,77.843750,172.218750,384.000000]
t_13 = [29.000000,17.000000,18.250000,27.750000,32.125000,69.625000,183.453125,324.000000]
t_14 = [17.000000,13.500000,27.250000,32.500000,50.375000,89.656250,198.781250,324.000000]
t_15 = [15.000000,24.000000,29.500000,41.500000,66.625000,101.593750,202.000000,384.000000]



#Below are the theoretical mean and variances of T for different sample sizes

# sample sizeL 32
mu_32 = 15*(1-32/4096) + 32*0.0864257812
sigma_32 = math.sqrt((2.0/15)*(15*(1-32/4096)+32*0.0864257812)**2)


# sample sizeL 64
mu_64 = 15*(1-64/4096) + 64*0.0864257812
sigma_64 = math.sqrt((2.0/15)*(15*(1-64/4096)+64*0.0864257812)**2)


# sample sizeL 128
mu_128 = 15*(1-128/4096) + 128*0.0864257812
sigma_128 = math.sqrt((2.0/15)*(15*(1-128/4096)+128*0.0864257812)**2)


# sample sizeL 256
mu_256 = 15*(1-256/4096) + 256*0.0864257812
sigma_256 = math.sqrt((2.0/15)*(15*(1-256/4096)+256*0.0864257812)**2)


# sample sizeL 512
mu_512 = 15*(1-512/4096) + 512*0.0864257812
sigma_512 = math.sqrt((2.0/15)*(15*(1-512/4096)+512*0.0864257812)**2)


# sample sizeL 1024
mu_1024 = 15*(1-1024/4096) + 1024*0.0864257812
sigma_1024 = math.sqrt((2.0/15)*(15*(1-1024/4096)+1024*0.0864257812)**2)


# sample sizeL 2048
mu_2048 = 15*(1-2048/4096) + 2048*0.0864257812
sigma_2048 = math.sqrt((2.0/15)*(15*(1-2048/4096)+2048*0.0864257812)**2)


# sample sizeL 4096
mu_4096 = 15*(1-4096/4096) + 4096*0.0864257812
sigma_4096 = math.sqrt((2.0/15)*(15*(1-4096/4096)+4096*0.0864257812)**2)


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
plt.title('$T(\phi,a)$ in SMALLPRESENT-4 with all zero key upto 2 rounds')
plt.text(5.2,78,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(5.2,85,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(5.2,99,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([5, 12, 0, 120])
plt.grid(True)
plt.show()
