import numpy as np

def LOS_loss(fc,d):
    '''
    Here d is in units of kilometers, and fc is the carrier frequency in MHz
    '''

    if (d<0.02) or (d>5):
        raise Exception("Distance out of range")
    elif ( fc<800 ) or (fc>2000):
        raise Exception("Frequency out of range")

    p = 42.6 + 26*np.log(d) + 20*np.log(fc)

    return p
