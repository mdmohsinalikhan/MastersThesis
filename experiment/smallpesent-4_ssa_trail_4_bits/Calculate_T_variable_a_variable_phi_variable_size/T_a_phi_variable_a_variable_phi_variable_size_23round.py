import numpy as np
import matplotlib.pyplot as plt
import math

t = [5,6,7,8,9,10,11,12]

# evenly sampled time at 200ms intervals
t_0 = [11.0000,9.5000,8.0000,12.5000,9.0625,8.6875,14.8594,11.7578]
t_1 = [11.0000,12.0000,14.2500,11.0000,15.1250,12.8438,6.7031,9.1641]
t_2 = [14.0000,11.0000,9.7500,11.1250,10.3750,11.6562,5.4062,10.9141]
t_3 = [16.0000,11.0000,14.0000,18.1250,13.3125,11.3438,7.6562,10.1719]
t_4 = [20.0000,24.5000,18.5000,19.2500,16.8125,16.6250,12.5625,6.8672]
t_5 = [33.0000,23.5000,18.0000,14.1250,15.8750,14.4375,12.7344,9.2188]
t_6 = [9.0000,14.0000,13.7500,18.3750,18.0000,19.3438,19.5000,14.9688]
t_7 = [6.0000,10.0000,13.5000,17.3750,12.0625,7.6250,15.3438,13.1328]
t_8 = [16.0000,10.0000,23.5000,14.6250,20.5625,18.6250,21.2188,21.1953]
t_9 = [18.0000,13.0000,13.5000,14.3750,16.5000,10.1875,12.4531,9.9297]
t_a = [15.0000,11.0000,13.2500,5.2500,6.0000,4.1562,7.2969,7.6406]
t_b = [34.0000,19.5000,13.0000,8.0000,3.8125,7.9062,15.4844,18.1406]
t_c = [20.0000,15.5000,7.0000,12.3750,7.6875,19.0938,18.6875,21.8594]
t_d = [18.0000,21.5000,13.0000,12.3750,22.3750,22.1250,13.8594,10.9062]
t_e = [13.0000,9.0000,10.7500,9.7500,9.6875,10.0625,4.5156,5.7734]
t_f = [8.0000,10.5000,16.5000,8.5000,6.5000,10.9688,16.8281,12.7812]


#Sample size 32
mu_32, sigma_32 = (15+32*0.002966642379761), math.sqrt((2.0/15.0)*(15+32*0.002966642379761)**2)
print mu_32,sigma_32
x_32 = mu_32 + sigma_32 * np.random.randn(200)

#Sample size 64
mu_64, sigma_64 = (15+64*0.002966642379761), math.sqrt((2.0/15.0)*(15+64*0.002966642379761)**2)
x_64 = mu_64 + sigma_64 * np.random.randn(200)

#Sample size 128
mu_128, sigma_128 = (15+128*0.002966642379761), math.sqrt((2.0/15.0)*(15+128*0.002966642379761)**2)
x_128 = mu_128 + sigma_128 * np.random.randn(200)

#Sample size 256
mu_256, sigma_256 = (15+256*0.002966642379761), math.sqrt((2.0/15.0)*(15+256*0.002966642379761)**2)
x_256 = mu_256 + sigma_256 * np.random.randn(200)

#Sample size 512
mu_512, sigma_512 = (15+512*0.002966642379761), math.sqrt((2.0/15.0)*(15+512*0.002966642379761)**2)
x_512 = mu_512 + sigma_512 * np.random.randn(200)

#Sample size 1024
mu_1024, sigma_1024 = (15+1024*0.002966642379761), math.sqrt((2.0/15.0)*(15+1024*0.002966642379761)**2)
x_1024 = mu_1024 + sigma_1024 * np.random.randn(200)

#Sample size 2048
mu_2048, sigma_2048 = (15+2048*0.002966642379761), math.sqrt((2.0/15.0)*(15+2048*0.002966642379761)**2)
x_2048 = mu_2048 + sigma_2048 * np.random.randn(200)

#Sample size 4096
mu_4096, sigma_4096 = (15+4096*0.002966642379761), math.sqrt((2.0/15.0)*(15+4096*0.002966642379761)**2)
x_4096 = mu_4096 + sigma_4096 * np.random.randn(200)

#for x in range(0,200):
#	line1 = []	
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
plt.title('$T(\phi,a)$ in SMALLPRESENT-4 with all zero key upto 23 rounds')
plt.text(5.2,78,'For all $\phi_1,\phi_2$ if $|\phi_1|=|\phi_2|$ then $\phi_1 = \phi_2$')
plt.text(5.2,85,'For all $\phi_1,\phi_2$ if $|\phi_1| < |\phi_2|$ then $\phi_1 \subset \phi_2$')
plt.text(5.2,92,'The dark gray portion is 1 standard deviation around mean of $T(\phi,a)$')
plt.text(5.2,99,'The light gray portion is 2 standard deviation around mean of $T(\phi,a)$')
plt.axis([5, 12, 0, 120])
plt.grid(True)
plt.show()
