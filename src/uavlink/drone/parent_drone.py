from uavlink.drone import drone


class parent_drone(drone):
    def __init__(self, id, charge, pos, v,rf = 1):
        '''
        Initialize the drone.
        self.id -> drone unique ID
        self.charge -> drone charge
        self.pos -> drone position as [x,y,z]
        self.v -> drone velocity as [x,y,z]
        self.rf -> drone reliability factor [Optional]
        '''
        super().__init__(id, charge, pos, v)
        self.set_rf(rf)
    
    def set_sf(self, sf):
        '''
        Set the stability factor of the drone.
        '''
        self.sf = sf
    
    def set_plf(self, plf):
        '''
        Set the primary link factor of the drone.
        '''
        self.plf = plf
    
    def set_slf(self, slf):
        '''
        Set the secondary link factor of the drone.
        '''
        self.slf = slf
    
    def set_cf(self, cf):
        '''
        Set the charge factor of the drone.
        '''
        self.cf = cf
    
    def set_rf(self, rf):
        '''
        Set the reliability factor of the drone.
        '''
        self.rf = rf
    
    def set_Cf(self, Cf):
        '''
        Set the connection factor of the drone.
        '''
        self.Cf = Cf