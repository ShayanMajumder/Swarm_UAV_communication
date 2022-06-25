import uavlink as ul
import numpy as np
import matplotlib.pyplot as plt


fc = 2000 # f is the carrier frequency in mhz
P_urban = []
distances = np.arange(0.02,5,0.01)

for d in distances:
    p = ul.linkbudget.NLOS_loss(fc,d, w = np.random.randint(5,20) , hm = np.random.randint(1,3),hb = np.random.randint(4,50),hr = np.random.randint(50,100), phi = np.random.randint(0,90), dense = (np.random.rand() > 0.5), b = np.random.randint(5,20))
    P_urban.append(p)

plt.plot(distances,P_urban)
plt.legend(["NLOS"])
plt.xlabel('Distance in Kms')
plt.ylabel('Power loss in dB')
plt.title("Non Line of Sight Link Loss dynamic")
plt.show()