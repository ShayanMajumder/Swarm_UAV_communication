import uavlink as ul
import numpy as np
import matplotlib.pyplot as plt

fc = 2000 # f is the carrier frequency in mhz
P1 = []
P2 = []
P3 = []
distances = np.arange(0.02,5,0.01)

for d in distances:
    P1.append(ul.linkbudget.LOS_loss(fc,d))
    p = ul.linkbudget.NLOS_loss(fc,d)
    P2.append(p)
    p = ul.linkbudget.NLOS_loss(fc,d, w = np.random.randint(5,20) , hm = np.random.randint(1,3),hb = np.random.randint(4,50),hr = np.random.randint(50,100), phi = np.random.randint(0,90), dense = (np.random.rand() > 0.5), b = np.random.randint(5,20))   
    P3.append(p)
    

plt.plot(distances,P1)
plt.plot(distances,P2)
plt.plot(distances,P3)
plt.legend(["LOS","NLOS","NLOS_dynamic"])
plt.xlabel('Distance in Kms')
plt.ylabel('Power loss in dB')
plt.title("LOS vs NLOS vs NLOS_dynamic losses")
plt.show()