class drone:
  def __init__(self, id, charge, pos, v):
    '''
    Initialize the drone.
    self.id -> drone unique ID
    self.charge -> drone charge
    self.pos -> drone position as [x,y,z]
    self.v -> drone velocity as [x,y,z]
    '''
    self.id = id
    self.charge = charge
    self.pos = pos
    self.v = v
