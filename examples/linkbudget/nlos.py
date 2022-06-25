import uavlink as ul
import numpy as np
import matplotlib.pyplot as plt


fc = 2000 # f is the carrier frequency in mhz
P_urban = []
distances = np.arange(0.02,5,0.01)

for d in distances:
    p = ul.linkbudget.NLOS_loss(fc,d)
    P_urban.append(p)

plt.plot(distances,P_urban)
plt.legend(["NLOS"])
plt.xlabel('Distance in Kms')
plt.ylabel('Power loss in dB')
plt.title("Non Line of Sight Link Loss")
plt.show()