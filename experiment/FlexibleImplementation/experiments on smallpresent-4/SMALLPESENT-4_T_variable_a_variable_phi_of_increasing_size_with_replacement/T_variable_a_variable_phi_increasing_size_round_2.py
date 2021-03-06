import numpy as np
import matplotlib.pyplot as plt
import math


t = [5,6,7,8,9,10,11,12]


#Creating the list. Logorithm of sample size. Will be plotted in x-axist_0 = [22.000000,28.500000,23.250000,41.875000,66.937500,128.531250,237.343750,445.351562]
t_1 = [20.000000,16.000000,20.500000,27.375000,30.750000,60.781250,147.406250,255.718750]
t_2 = [24.000000,26.500000,24.500000,32.500000,65.562500,126.843750,180.140625,317.117188]
t_3 = [20.000000,22.500000,25.000000,33.250000,61.812500,107.093750,215.484375,408.414062]
t_4 = [13.000000,20.500000,19.250000,23.500000,66.125000,110.906250,173.875000,312.843750]
t_5 = [17.000000,24.000000,23.250000,50.750000,72.187500,111.437500,189.171875,370.539062]
t_6 = [17.000000,22.500000,20.250000,22.375000,57.000000,130.000000,213.890625,362.710938]
t_7 = [15.000000,8.500000,19.000000,30.000000,66.250000,128.250000,199.187500,348.195312]
t_8 = [15.000000,10.500000,22.750000,30.250000,45.562500,83.687500,140.921875,311.398438]
t_9 = [21.000000,15.000000,33.500000,53.750000,90.750000,144.843750,224.781250,416.562500]
t_10 = [20.000000,26.500000,28.250000,40.500000,60.937500,125.593750,208.531250,353.164062]
t_11 = [6.000000,14.500000,16.250000,15.875000,41.000000,99.187500,193.078125,334.937500]
t_12 = [17.000000,23.000000,18.000000,36.500000,67.437500,87.781250,186.015625,356.843750]
t_13 = [35.000000,21.000000,16.000000,27.125000,56.000000,100.062500,203.390625,351.835938]
t_14 = [15.000000,12.000000,12.000000,23.625000,60.125000,99.687500,194.781250,337.265625]
t_15 = [19.000000,18.500000,23.750000,22.625000,48.937500,73.656250,159.937500,372.054688]



#Below are the theoretical mean and variances of T for different sample sizes

# sample sizeL 32
mu_32 = 15 + 32*.0864257812
sigma_32 = math.sqrt((2.0/15)*(15+32*.0864257812)**2)


# sample sizeL 64
mu_64 = 15 + 64*.0864257812
sigma_64 = math.sqrt((2.0/15)*(15+64*.0864257812)**2)


# sample sizeL 128
mu_128 = 15 + 128*.0864257812
sigma_128 = math.sqrt((2.0/15)*(15+128*.0864257812)**2)


# sample sizeL 256
mu_256 = 15 + 256*.0864257812
sigma_256 = math.sqrt((2.0/15)*(15+256*.0864257812)**2)


# sample sizeL 512
mu_512 = 15 + 512*.0864257812
sigma_512 = math.sqrt((2.0/15)*(15+512*.0864257812)**2)


# sample sizeL 1024
mu_1024 = 15 + 1024*.0864257812
sigma_1024 = math.sqrt((2.0/15)*(15+1024*.0864257812)**2)


# sample sizeL 2048
mu_2048 = 15 + 2048*.0864257812
sigma_2048 = math.sqrt((2.0/15)*(15+2048*.0864257812)**2)


# sample sizeL 4096
mu_4096 = 15 + 4096*.0864257812
sigma_4096 = math.sqrt((2.0/15)*(15+4096*.0864257812)**2)


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
