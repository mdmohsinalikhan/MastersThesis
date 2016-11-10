import numpy as np
import matplotlib.pyplot as plt
import math

t = [5,6,7,8,9,10,11,12]

# evenly sampled time at 200ms intervals
t_0 = [16.0000,20.5000,15.5000,19.3750,29.1250,24.2812,25.2812,48.5000]
t_1 = [19.0000,16.5000,11.2500,29.5000,15.3750,32.0938,46.8438,87.1641]
t_2 = [12.0000,16.5000,18.2500,21.0000,17.7500,27.8125,32.6562,82.5312]
t_3 = [9.0000,15.0000,18.0000,13.7500,33.3750,63.8750,74.8750,95.9375]
t_4 = [17.0000,10.5000,12.7500,21.0000,26.1875,41.0938,72.6250,124.7188]
t_5 = [14.0000,18.5000,21.0000,21.6250,35.7500,51.4688,93.8750,151.1250]
t_6 = [18.0000,18.5000,27.5000,38.7500,33.6250,37.3750,67.5469,147.4297]
t_7 = [27.0000,19.5000,26.2500,26.6250,36.2500,53.7500,73.5625,86.2656]
t_8 = [21.0000,14.5000,16.5000,23.0000,24.9375,29.0938,49.1562,69.3125]
t_9 = [26.0000,20.0000,17.0000,21.8750,30.3750,63.9688,113.2812,173.7031]
t_a = [25.0000,24.5000,16.0000,21.8750,26.3125,32.6562,70.7188,141.5703]
t_b = [20.0000,25.0000,19.7500,20.1250,35.5000,59.2812,72.7656,156.5625]
t_c = [30.0000,32.0000,34.2500,34.1250,51.1250,46.5938,41.0781,57.0156]
t_d = [12.0000,20.0000,17.5000,10.3750,16.2500,31.7188,54.3125,89.4297]
t_e = [16.0000,14.0000,13.7500,20.3750,29.2500,43.9688,44.8594,85.4297]
t_f = [11.0000,13.5000,13.5000,16.5000,35.6875,59.7188,78.6250,128.2188]

#Sample size 32
mu_32, sigma_32 = (15+32*0.003517270088196), math.sqrt((2.0/15.0)*(15+32*0.003517270088196)**2)
print mu_32,sigma_32
x_32 = mu_32 + sigma_32 * np.random.randn(200)

#Sample size 64
mu_64, sigma_64 = (15+64*0.003517270088196), math.sqrt((2.0/15.0)*(15+64*0.003517270088196)**2)
x_64 = mu_64 + sigma_64 * np.random.randn(200)

#Sample size 128
mu_128, sigma_128 = (15+128*0.003517270088196), math.sqrt((2.0/15.0)*(15+128*0.003517270088196)**2)
x_128 = mu_128 + sigma_128 * np.random.randn(200)

#Sample size 256
mu_256, sigma_256 = (15+256*0.003517270088196), math.sqrt((2.0/15.0)*(15+256*0.003517270088196)**2)
x_256 = mu_256 + sigma_256 * np.random.randn(200)

#Sample size 512
mu_512, sigma_512 = (15+512*0.003517270088196), math.sqrt((2.0/15.0)*(15+512*0.003517270088196)**2)
x_512 = mu_512 + sigma_512 * np.random.randn(200)

#Sample size 1024
mu_1024, sigma_1024 = (15+1024*0.003517270088196), math.sqrt((2.0/15.0)*(15+1024*0.003517270088196)**2)
x_1024 = mu_1024 + sigma_1024 * np.random.randn(200)

#Sample size 2048
mu_2048, sigma_2048 = (15+2048*0.003517270088196), math.sqrt((2.0/15.0)*(15+2048*0.003517270088196)**2)
x_2048 = mu_2048 + sigma_2048 * np.random.randn(200)

#Sample size 4096
mu_4096, sigma_4096 = (15+4096*0.003517270088196), math.sqrt((2.0/15.0)*(15+4096*0.003517270088196)**2)
x_4096 = mu_4096 + sigma_4096 * np.random.randn(200)

#for x in range(0,200):
#	line1 = []	
#	line1.append(x_32[x])
#	line1.append(x_64[x])
#	line1.append(x_128[x])
#	line1.append(x_256[x])
#	line1.append(x_512[x])
#	line1.append(x_1024[x])
#	line1.append(x_2048[x])
#	line1.append(x_4096[x])
#	plt.plot(t,line1,'y--')

expected_T_a = []
expected_T_a.append(mu_32)
expected_T_a.append(mu_64)
expected_T_a.append(mu_128)
expected_T_a.append(mu_256)
expected_T_a.append(mu_512)
expected_T_a.append(mu_1024)
expected_T_a.append(mu_2048)
expected_T_a.append(mu_4096)

plt.plot(t,expected_T_a,linewidth=.1, linestyle="-", c="DimGray")

expected_T_a1 = []
expected_T_a1.append(mu_32+sigma_32)
expected_T_a1.append(mu_64+sigma_64)
expected_T_a1.append(mu_128+sigma_128)
expected_T_a1.append(mu_256+sigma_256)
expected_T_a1.append(mu_512+sigma_512)
expected_T_a1.append(mu_1024+sigma_1024)
expected_T_a1.append(mu_2048+sigma_2048)
expected_T_a1.append(mu_4096+sigma_4096)

plt.plot(t,expected_T_a1,linewidth=.1, linestyle="-", c="DimGray")

expected_T_a2 = []
expected_T_a2.append(mu_32-sigma_32)
expected_T_a2.append(mu_64-sigma_64)
expected_T_a2.append(mu_128-sigma_128)
expected_T_a2.append(mu_256-sigma_256)
expected_T_a2.append(mu_512-sigma_512)
expected_T_a2.append(mu_1024-sigma_1024)
expected_T_a2.append(mu_2048-sigma_2048)
expected_T_a2.append(mu_4096-sigma_4096)

plt.plot(t,expected_T_a2,linewidth=.1, linestyle="-", c="DimGray")


expected_T_a3 = []
expected_T_a3.append(mu_32+2*sigma_32)
expected_T_a3.append(mu_64+2*sigma_64)
expected_T_a3.append(mu_128+2*sigma_128)
expected_T_a3.append(mu_256+2*sigma_256)
expected_T_a3.append(mu_512+2*sigma_512)
expected_T_a3.append(mu_1024+2*sigma_1024)
expected_T_a3.append(mu_2048+2*sigma_2048)
expected_T_a3.append(mu_4096+2*sigma_4096)

plt.plot(t,expected_T_a3,linewidth=.1, linestyle="-", c="DimGray")

expected_T_a4 = []
expected_T_a4.append(mu_32-2*sigma_32)
expected_T_a4.append(mu_64-2*sigma_64)
expected_T_a4.append(mu_128-2*sigma_128)
expected_T_a4.append(mu_256-2*sigma_256)
expected_T_a4.append(mu_512-2*sigma_512)
expected_T_a4.append(mu_1024-2*sigma_1024)
expected_T_a4.append(mu_2048-2*sigma_2048)
expected_T_a4.append(mu_4096-2*sigma_4096)

plt.plot(t,expected_T_a4,linewidth=.1, linestyle="-", c="DimGray")

# red dashes, blue squares and green triangles
plt.plot(t, t_0, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_1, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_2, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_3, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_4, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_5, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_6, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_7, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_8, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_9, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_a, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_b, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_c, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_d, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_e, linewidth=.1, linestyle="-", c="red")
plt.plot(t, t_f, linewidth=.1, linestyle="-", c="red")

plt.fill_between(t, expected_T_a1,expected_T_a2,color='DimGray',alpha=.7)
plt.fill_between(t, expected_T_a1,expected_T_a3,color='DimGray',alpha=.35)
plt.fill_between(t, expected_T_a2,expected_T_a4,color='DimGray',alpha=.35)


plt.xlabel('$log_2(|\phi|)$')
plt.ylabel('$T(\phi,a)$')
plt.title('$T(\phi,a)$ in SMALLPRESENT-4 with all zero key upto 03 rounds')
plt.text(5.2,78,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(5.2,85,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(5.2,99,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([5, 12, 0, 120])
plt.grid(True)
plt.show()
