import numpy as np

class Q_grid:


    def __init__(self,params,lattice,sphere_mesh):


        if params.dQ == False:
            try:
                self.Q_steps = np.array(list(params.Q))
            except:
                self.Q_steps = np.array([params.Q])
        else:
            self.Q_steps = np.arange(params.dQ,params.Q_max,params.dQ)
        self.num_Q_steps = self.Q_steps.shape[0]
        print(f'\n ** number of Q steps **\n {self.num_Q_steps:d}\tOH MY!!\n')

        #self._mesh_points(params,lattice,sphere_mesh)
        self._mesh_points(params,lattice,sphere_mesh)



    def _mesh_points(self,params,lattice,sphere_mesh):
        
        self.num_mesh_points = np.zeros(self.num_Q_steps).astype(int)

        if params.dQ != False:

            for i in range(self.num_Q_steps):
                """
                scale number of points to keep density approximatly constant:
                N_1/4/pi/1**2 = N_2/4/pi/r_i**2 => N_2 = N_1 * r_i**2

                """
                self.num_mesh_points[i] = int(params.num_points*self.Q_steps[i]**2) 
            self.total_mesh_points = self.num_mesh_points.sum()

        else:

            self.num_mesh_points[:] = params.num_points
            self.total_mesh_points = self.num_mesh_points.sum()

        print(f'\n ** total mesh points **\n {self.total_mesh_points:d}\tWOW!!\n')


        for i in range(self.num_Q_steps):

            """ 
            sample points on the unit sphere. the number of points is calculated above 
            based on num_points given in main. x,y,z coords are then scaled so that 
            sqrt(x**2+y**2+z**2) == |Q_i|, where |Q_i| is the momentum transfer that
            we care about. 

            For FCC

            x' = 1/2/b*[b_2+b_3]  # cartesian
            y' = 1/2/b*[b_1+b_3]  # cartesian
            z' = 1/2/b*[b_2+b_1]  # cartesian
            r = xx' + yy' + zz'   # cartesian
            r = x(1/2/b*[b_2+b_3]) + y(1/2/b*[b_1+b_3]) + z(1/2/b*[b_2+b_1])
            r = 1/2/b*(y+z)*b_1 + 1/2/b*(x+z)*b_2 + 1/2/b*(x+y)*b_3
            r = Q_1*b_1 + Q_2*b_2 + Q_3*b_3 # r_lat basis
            only works for FCC using the lattice vectors I defined


            """

            self.Q_vecs = np.zeros((self.num_mesh_points[i],3))
            sphere_mesh.golden_spiral(self.num_mesh_points[i]) # points on unit sphere
            sphere_mesh.mesh = sphere_mesh.mesh*self.Q_steps[i] # scale radius to |Q|
            
            self.Q_vecs[:,0] = sphere_mesh.mesh[:,1]+sphere_mesh.mesh[:,2]
            self.Q_vecs[:,1] = sphere_mesh.mesh[:,2]+sphere_mesh.mesh[:,0]
            self.Q_vecs[:,2] = sphere_mesh.mesh[:,0]+sphere_mesh.mesh[:,1]
            self.Q_vecs = self.Q_vecs/2/lattice.rlat_const
            
            np.savetxt(f'Q_vecs_{i:04g}.txt',self.Q_vecs,fmt='%3.4f',
                    header=f'{self.Q_steps[i]:3.4f}')



 

        




