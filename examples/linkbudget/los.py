import uavlink as ul
import numpy as np
import matplotlib.pyplot as plt

fc = 2000 # f is the carrier frequency in mhz
P_urban = []
distances = np.arange(0.02,5,0.01)

for d in distances:
    P_urban.append(ul.linkbudget.LOS_loss(fc,d))

plt.plot(distances,P_urban)
plt.legend(["LOS"])
plt.xlabel('Distance in Kms')
plt.ylabel('Power loss in dB')
plt.title("Line of Sight Link Loss")
plt.show()
