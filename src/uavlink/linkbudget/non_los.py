import numpy as np

def NLOS_loss(fc,d, w = 12, hm = 2,hb = 26,hr = 75, phi = 45, dense = False, b = 12):
    '''
    Here d is in units of kilometers, fc is the carrier frequency in MHz,
    w is the width of the valley in meters, hm is eight of MS antenna,
    hb is height of the base antenna, hr is height of the obstacle
    phi is the angle between the street orientation and the direction of incidence in degrees
    dense tells the density of the place, b is distance between objects

    '''

    if ((d<0.02) or (d>5)):
        raise Exception("Distance out of range")
    elif ((fc<800) or (fc>2000)):
        raise Exception("Frequency out of range")
    elif ((hm<1) or (hm>3)):
        raise Exception("Hm out of range")
    elif ((hb<4) or (hb>50)):
        raise Exception("Hb out of range")
    elif ((phi<0) or (phi>90)):
        raise Exception("phi out of range")

    p_fspl = 32.4 + 20*np.log(d) + 20*np.log(fc) # free space path loss

    '''
    Orientation of the path is taken into account by an empirical correction factor L_ori
    '''
    if ((phi>=0) and (phi<=30)):
        L_ori = -10 + 0.354*phi
    elif ((phi>=35) and (phi<=55)):
        L_ori = 2.5 + 0.075*(phi -35)
    else:
        L_ori = 4 - 0.114*(phi - 55)
    
    del_h = np.abs(hr-hm)
    L_rts = -16.9 - 10*np.log(w) + 10*np.log(fc) + 20*np.log(del_h) + L_ori

    if (hb>hr):
        L_bsh = 18*np.log(1+del_h)
    else:
        L_bsh = 0
    
    if (hb>hr):
        ka = 54
    elif ((d>=0.5) and (hb<=hr)):
        ka = 54 - 0.5*del_h
    else:
        ka = 54 - (0.8*del_h*d)/0.5

    if (hb>hr):
        kd = 18
    else:
        kd = 18 - (15*del_h)/hr 

    if dense:
        kf = 1.5*(fc/925 - 1)
    else:
        kf = 0.7*(fc/925 - 1)

    L_msd = L_bsh + ka + kd*(np.log(d)) + kf*(np.log(fc)) - 9*np.log(b+1)

    if (L_rts + L_msd) > 0:
        p = p_fspl + L_rts + L_msd
    else:
        p = p_fspl

    return p


