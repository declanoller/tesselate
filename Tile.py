import numpy as np


class Tile:



    def __init__(self,pos,type=1,rot=0):

        #pos is an x,y coordinate. For a 2x2, it's the position of the bottom left.
        #type 1 is the 1x1, type 2 is the 2x2
        #rotation=0 is the default, and the other rotations are 1,2,3, for rotating 90 degrees CCW.
        self.pos = pos
        self.type = type
        self.rot = rot

        ind = (np.array(list(range(12))) - 3*self.rot)%12
        match = (np.array([11,2,1, 5,9,3, 10,8,7, 4,6,0]) - 3*self.rot)%12

        self.pair_match = dict(zip(ind,match))










#
