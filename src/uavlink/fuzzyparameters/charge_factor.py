import numpy as np
from uavlink.engine.concentrate_dilate import concentrate_dilate

def cf(parentdrones,childdrones,c_d = 1):
    
    for i in range(len(parentdrones)):
        charges = []
        for pdv in parentdrones:
            if pdv.id != parentdrones[i].id:
                charges.append((parentdrones[i].charge + pdv.charge)/2)
                
        
        for cdv in childdrones:
            charges.append((parentdrones[i].charge + cdv.charge)/2)
            
        
        c_rms = np.sqrt(np.mean(np.array(charges)**2))  # Root mean square
        parentdrones[i].set_cf(concentrate_dilate(c_rms/100,c_d))

'''class drone:
  def __init__(self, charge):
    self.charge = charge
    self.cf = 1

parentdrones = []
childdrones = []

for i in range(1,6):
    parentdrones.append(drone(i*20))
    childdrones.append(drone(i*20))

cf(parentdrones,childdrones)

for i in range(5):
    print(parentdrones[i].cf)'''

