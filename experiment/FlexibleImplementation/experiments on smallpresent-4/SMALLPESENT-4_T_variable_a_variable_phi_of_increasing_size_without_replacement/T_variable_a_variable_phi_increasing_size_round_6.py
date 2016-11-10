import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12]


#Creating the list. Logorithm of sample size. Will be plotted in x-axist_0 = [21.000000,23.000000,18.750000,15.125000,15.875000,11.781250,12.593750,13.312500]
t_1 = [11.000000,17.000000,20.500000,12.250000,23.937500,10.562500,15.984375,15.945312]
t_2 = [13.000000,23.000000,18.250000,12.375000,16.312500,13.156250,18.625000,23.429688]
t_3 = [15.000000,21.000000,27.000000,34.375000,28.750000,31.750000,25.421875,14.015625]
t_4 = [17.000000,17.500000,19.250000,23.625000,28.437500,20.062500,15.484375,16.640625]
t_5 = [11.000000,12.000000,18.750000,14.125000,13.125000,18.437500,13.031250,3.484375]
t_6 = [12.000000,18.000000,10.000000,11.500000,12.687500,10.500000,16.968750,13.093750]
t_7 = [7.000000,16.500000,21.750000,19.375000,14.437500,22.625000,21.984375,19.109375]
t_8 = [17.000000,22.500000,14.000000,12.125000,9.062500,9.687500,10.843750,17.421875]
t_9 = [11.000000,10.000000,14.000000,15.500000,14.875000,9.687500,10.890625,17.976562]
t_10 = [40.000000,23.000000,12.500000,18.125000,12.750000,8.937500,13.359375,27.218750]
t_11 = [15.000000,9.500000,9.000000,14.125000,20.437500,26.906250,18.406250,12.679688]
t_12 = [13.000000,16.500000,18.500000,14.625000,25.562500,23.031250,14.406250,9.132812]
t_13 = [16.000000,16.000000,20.500000,22.625000,21.625000,24.187500,28.671875,27.968750]
t_14 = [13.000000,14.000000,11.750000,17.250000,15.625000,21.687500,14.562500,18.781250]
t_15 = [18.000000,38.000000,32.000000,31.250000,17.187500,10.250000,12.093750,10.937500]



#Below are the theoretical mean and variances of T for different sample sizes

# sample sizeL 32
mu_32 = 15*(1-32/4096) + 32*0.0039848089
sigma_32 = math.sqrt((2.0/15)*(15*(1-32/4096)+32*0.0039848089)**2)


# sample sizeL 64
mu_64 = 15*(1-64/4096) + 64*0.0039848089
sigma_64 = math.sqrt((2.0/15)*(15*(1-64/4096)+64*0.0039848089)**2)


# sample sizeL 128
mu_128 = 15*(1-128/4096) + 128*0.0039848089
sigma_128 = math.sqrt((2.0/15)*(15*(1-128/4096)+128*0.0039848089)**2)


# sample sizeL 256
mu_256 = 15*(1-256/4096) + 256*0.0039848089
sigma_256 = math.sqrt((2.0/15)*(15*(1-256/4096)+256*0.0039848089)**2)


# sample sizeL 512
mu_512 = 15*(1-512/4096) + 512*0.0039848089
sigma_512 = math.sqrt((2.0/15)*(15*(1-512/4096)+512*0.0039848089)**2)


# sample sizeL 1024
mu_1024 = 15*(1-1024/4096) + 1024*0.0039848089
sigma_1024 = math.sqrt((2.0/15)*(15*(1-1024/4096)+1024*0.0039848089)**2)


# sample sizeL 2048
mu_2048 = 15*(1-2048/4096) + 2048*0.0039848089
sigma_2048 = math.sqrt((2.0/15)*(15*(1-2048/4096)+2048*0.0039848089)**2)


# sample sizeL 4096
mu_4096 = 15*(1-4096/4096) + 4096*0.0039848089
sigma_4096 = math.sqrt((2.0/15)*(15*(1-4096/4096)+4096*0.0039848089)**2)


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
plt.title('$T(\phi,a)$ in SMALLPRESENT-4 with all zero key upto 6 rounds')
plt.text(5.2,78,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(5.2,85,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(5.2,99,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([5, 12, 0, 120])
plt.grid(True)
plt.show()
