import numpy as np
import matplotlib.pyplot as plt
import math

t = [5,6,7,8,9,10,11,12]

# evenly sampled time at 200ms intervals
t_0 = [14.0000,11.5000,7.2500,15.1250,24.4375,26.5625,8.4844,7.1641]
t_1 = [32.0000,23.0000,13.7500,16.3750,15.1250,13.1562,10.9062,6.9922]
t_2 = [10.0000,12.0000,13.5000,15.1250,12.8125,19.6875,9.3281,11.2500]
t_3 = [24.0000,15.5000,10.0000,9.0000,10.5000,15.7812,13.8594,12.8047]
t_4 = [17.0000,21.5000,31.0000,17.2500,13.0000,13.0000,5.4219,5.9062]
t_5 = [9.0000,15.5000,8.5000,12.8750,13.5000,13.2500,12.5312,10.9062]
t_6 = [13.0000,13.5000,9.0000,14.2500,9.5625,8.2812,8.4062,10.5391]
t_7 = [17.0000,21.0000,26.5000,20.1250,26.0000,30.9688,30.3906,42.5703]
t_8 = [11.0000,12.0000,9.2500,10.1250,9.9375,15.7500,18.9844,23.1406]
t_9 = [9.0000,9.0000,23.7500,20.8750,14.1250,19.8125,17.4219,14.4922]
t_a = [24.0000,23.0000,22.0000,14.1250,14.3750,28.2500,21.9062,14.3672]
t_b = [15.0000,18.0000,16.7500,14.0000,13.2500,14.9062,14.8906,6.1562]
t_c = [9.0000,16.0000,20.2500,17.2500,13.1250,8.2812,9.4219,9.5234]
t_d = [9.0000,16.5000,9.7500,9.5000,21.0625,29.1250,29.0000,19.0547]
t_e = [14.0000,18.5000,11.2500,13.8750,16.5625,23.9062,19.7656,17.5469]
t_f = [8.0000,10.0000,7.7500,7.5000,10.7500,6.7812,13.3125,18.0938]

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
plt.title('$T(\phi,a)$ in SMALLPRESENT-4 with all zero key upto 22 rounds')
plt.text(5.2,78,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(5.2,85,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(5.2,99,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([5, 12, 0, 120])
plt.grid(True)
plt.show()
