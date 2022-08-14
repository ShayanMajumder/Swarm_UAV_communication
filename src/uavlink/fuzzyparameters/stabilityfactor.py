import numpy as np
from uavlink.engine.concentrate_dilate import concentrate_dilate
from uavlink.engine.compliment import compliment

def sf(parentdrones,childdrones,v_max,cd = 1):
    
    v_mean = 0
    for i in range(len(parentdrones)):
        pd_mean = 0
        for pdv in parentdrones:
            pd_mean = pd_mean + np.linalg.norm(np.array(pdv.v)-np.array(parentdrones[i].v))
        
        #pd_mean = pd_mean/(len(parentdrones)-1)

        cd_mean = 0
        for cdv in childdrones:
            cd_mean = cd_mean + np.linalg.norm(np.array(cdv.v)-np.array(parentdrones[i].v))
        
        #cd_mean = (cd_mean + pd_mean)

        pv_mean = (pd_mean + cd_mean)/(len(childdrones) + len(parentdrones)-1)
        #parentdrones[i].set_sf((1-pv_mean/v_max))
        parentdrones[i].set_sf(compliment(concentrate_dilate(pv_mean/v_max,cd)))

'''class drone:
    def __init__(self, v):
        self.v = v

    def set_sf(self, sf):
        self.sf = sf

parentdrones = []
childdrones = []

for i in range(5):
    parentdrones.append(drone([5,6,7]))
    childdrones.append(drone([1,5,-3]))

sf(parentdrones,childdrones,500)

for i in range(5):
    print(parentdrones[i].sf)'''

