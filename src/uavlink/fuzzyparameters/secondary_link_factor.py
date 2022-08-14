import numpy as np
import uavlink as ul
from uavlink.engine.concentrate_dilate import concentrate_dilate
from uavlink.engine.compliment import compliment

def slf(parentdrones,childdrones,d_max = 5,frequency = 2400, cd1 = 1, cd2 = 1):
    power_max = ul.linkbudget.NLOS_loss(frequency,d_max)
    
    for i in range(len(parentdrones)):
        links = []
        missing_drone = 0
        for pdv in parentdrones:
            if pdv.id != parentdrones[i].id:
                try:
                    distance = np.linalg.norm(np.array(pdv.pos)-np.array(parentdrones[i].pos))
                    links.append(ul.linkbudget.LOS_loss(frequency,distance))
                except Exception as e:
                    if str(e) == "DistanceOutOfRange":
                        missing_drone = missing_drone + 1
                    else:
                        raise e
                    
                
        
        for cdv in childdrones:
            try:
                distance = np.linalg.norm(np.array(cdv.pos)-np.array(parentdrones[i].pos))
                links.append(ul.linkbudget.NLOS_loss(frequency,distance,hb = parentdrones[i].pos[2]*1000))
            except Exception as e:
                    if str(e) == "DistanceOutOfRange":
                        missing_drone = missing_drone + 1
                    else:
                        raise e
        
        power_rms = np.sqrt(np.mean(np.array(links)**2))  # Root mean square
        # parentdrones[i].set_slf(1 - power_rms/power_max)
        # parentdrones[i].set_Cf(1 - (missing_drone/(len(parentdrones)+len(childdrones)-1)))
        parentdrones[i].set_slf(compliment(concentrate_dilate(power_rms/power_max,cd1)))
        parentdrones[i].set_Cf(compliment(concentrate_dilate(missing_drone/(len(parentdrones)+len(childdrones)-1),cd2)))
        


'''class drone:
  def __init__(self, pos, id):
    self.id = id
    self.slf = slf
    self.pos = pos
    self.cf = 1

parentdrones = []
childdrones = []

for i in range(1,7,1):
    parentdrones.append(drone([i,i,i+0.5],'PD'+str(i)))
    childdrones.append(drone([i,i,i],'CD'+str(i)))

slf(parentdrones,childdrones)

for i in range(len(parentdrones)):
    print(parentdrones[i].cf)
    print(parentdrones[i].slf)'''
