import numpy as np

class sphere_mesh:
    
    """
    this object contains points on the surface of a unit sphere. the idea is for them 
    to be *evenly* spaced. apparently this is impossible, so approximate sampling is used.
    right now, I am just gonna use the 'golden spiral algorithm' which I simply copied
    from stackoverflow.com/questions/9600801/evenly-distributing-n-points-on-a-sphere. 
    it allegedly does a pretty good job for a reasonably large number of points.
    """

    def __init__(self):

        pass

    def golden_spiral(self,num_points):
        
        self.mesh = np.zeros((num_points,3))

        dphi = np.pi*(3-np.sqrt(5)) # golden angle
        for i in range(num_points):
            y = 1-(i/(num_points-1))*2
            r = np.sqrt(1-y**2)
            theta = dphi*i
            x = np.cos(theta)*r
            z = np.sin(theta)*r
            self.mesh[i,:] = [x,y,z]
            

