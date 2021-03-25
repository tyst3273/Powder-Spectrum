import numpy as np

class params:

    def __init__(self,e_i=100,temp=300,dQ=False,Q=1,num_points=1000):

        ### constants
        hbar = 6.58212e-16*1e-3 # milli eV * s
        hbar_SI = 1.05457e-34 #J.s
        neutron_mass = 1.67492e-27 # kg
        j2meV = 6.24151e21 # joules to milli eV
        e2ksq = 2*neutron_mass/hbar_SI**2/j2meV/1e20 # k**2 = e2ksq*E, E in meV, k in 1/A
        

        # not constants
        self.temp = temp # K
        self.e_i = e_i # meV
        self.Q_max = 2*np.sqrt(e2ksq*e_i) # 1/Angstrom

        self.dQ = dQ
        self.Q = Q
        self.num_points = num_points # if dQ ==  False, density on the specified shell.
        # otherwise this is the points on a unit sphere and the number of points on 
        # each shell are scaled by the area to have approximately the same density
        # as there are points on the unit sphere. 













