"""

** NOTES **
1. can probably use symmetry to only sample (appropriately weighted) Q-points in 
    the 1st quadrant

2. in changing from cartesian (reciprocal) coords to reciprocal lattice vector coords,
    the relations I used ONLY WORK FOR FCC. specifically, only using the lattice vectors
    that I defined.

** INSTRUCTIONS **

set the lattice vectors and lattice constants and the incident energy (e_i). 
e_i determines the cutoff wave vector Q_max. if you want to sample a grid of
wave vector lengths |Q|, set dQ to the step bewtween wave vectors. the code will 
generate a list of Q_steps from dQ to Q_max with step size dQ. in this case, num_points
is the number of points on a UNIT sphere. The number of points on each sphere with radius
|Q_i| (the Q_step[i]) is determined by keeping the density of points on the surface 
approximately equal to the density on the UNIT sphere. the code will create a handful of 
files, one for each Q_step, named Q_vecs_*.txt. inside the files is a header which 
tells you |Q| and a list of Q vectors in reduced coords. i.e. an arbitrary point in 
Q space is determined from the Q vectors (Q1,Q2,Q3) according to 
v = Q1*b1+Q2*b2+Q3*b3, where Qi are the components of the Q vector and bi are the 
reciprocal lattice basis vectors. the text files containing the Q vectors can be 
directly read into SNAXS using the run_sqw_v2 and auto_sqw_v2 scripts. 

if you want to only sample a single |Q|, set dQ to false and Q to the |Q| you want to 
sample (in 1/Angstrom). the num_points is the number of points on the sphere with radius
|Q|, NOT the UNIT sphere. this will produce only 1 file, Q_vecs_0000.txt which contains
the same stuff specified above.

"""

import numpy as np
import SphereMesh
import Lattice
import Params
import QGrid

lat_vecs = [[0,1,1],[1,0,1],[1,1,0]]
lat_const = 1.991

e_i = 65 # meV
dQ = False # in 1/Angst
Q = [5.366,5.724,8.629] # in 1/Angst
num_points = 500000

params = Params.params(e_i=e_i,dQ=dQ,Q=Q,num_points=num_points)
lattice = Lattice.lattice(lat_const=lat_const,lat_vecs=lat_vecs)
sphere_mesh = SphereMesh.sphere_mesh()

Q_grid = QGrid.Q_grid(params,lattice,sphere_mesh)















