import numpy as np
from uavlink.engine.concentrate_dilate import concentrate_dilate
from uavlink.engine.compliment import compliment

def plf(parentdrones,childdrones,d_max = 5, c_d = 2):
    
    for i in range(len(parentdrones)):
        distances = []
        for pdv in parentdrones:
            if pdv.id != parentdrones[i].id:
                distances.append(np.linalg.norm(np.array(pdv.pos)-np.array(parentdrones[i].pos)))
                
        
        for cdv in childdrones:
            distances.append(np.linalg.norm(np.array(cdv.pos)-np.array(parentdrones[i].pos)))
            
        
        d_rms = np.sqrt(np.mean(np.array(distances)**2))
        parentdrones[i].set_plf(compliment(concentrate_dilate(d_rms/d_max,c_d)))

        


'''class drone:
  def __init__(self, pos):
    self.plf = plf
    self.pos = pos

parentdrones = []
childdrones = []

for i in range(5):
    parentdrones.append(drone([i,i,i+5]))
    childdrones.append(drone([i,i,i]))

plf(parentdrones,childdrones,10)

for i in range(5):
    print(parentdrones[i].plf)'''
