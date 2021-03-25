import numpy as np

class lattice:

    def __init__(self,lat_const=1,lat_vecs=[[1,0,0],[0,1,0],[0,0,1]]):

        lat_vecs = np.array(lat_vecs)*lat_const
        self.lat_vecs = lat_vecs
        cell_vol = lat_vecs[0,:].dot(np.cross(lat_vecs[1,:],lat_vecs[2,:]))

        rlat_vecs = np.zeros((3,3))
        rlat_vecs[0,:] = 2*np.pi*np.cross(lat_vecs[1,:],lat_vecs[2,:])/cell_vol
        rlat_vecs[1,:] = 2*np.pi*np.cross(lat_vecs[2,:],lat_vecs[0,:])/cell_vol
        rlat_vecs[2,:] = 2*np.pi*np.cross(lat_vecs[0,:],lat_vecs[1,:])/cell_vol

        self.rlat_vecs = rlat_vecs
        self.rlat_const = -rlat_vecs[0,0] # only for FCC using the lat_vecs I defined























