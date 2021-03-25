import numpy as np
import h5py
from scipy.io import loadmat
import matplotlib.pyplot as plt

num_e = 1000
e_max = 80

filename = 'out_0006_delta_fn.mat'
outfile = '1.0.dat'

dat = loadmat(filename)
strufacs = dat['s']
energies = dat['e']

num_Q = strufacs.shape[1]
num_b = strufacs.shape[0]

energy = np.linspace(0,e_max,num_e)
sqe = np.zeros(num_e)

for Q in range(num_Q):
    for b in range(num_b):
        index = np.argwhere(energy < energies[b,Q]).max()
        sqe[index] = sqe[index]+strufacs[b,Q]

fig,ax = plt.subplots()
fig.set_size_inches(6,4,forward=True)

ax.plot(energy,sqe,lw=1,color='k')

for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(1.5)
ax.minorticks_on()
ax.tick_params(which='both',width=1,labelsize='large')
ax.tick_params(which='major',length=5)
ax.tick_params(which='minor',length=2)

ax.set_xlabel('S(|Q|,w)',labelpad=4.0,fontweight='normal',fontsize='large')
ax.set_xlabel('Energy (meV)',labelpad=2.0,fontweight='normal',fontsize='large')

#plt.savefig('aluminum_powder_spectrum_slice.pdf',format='pdf',dpi=150,bbox_inches='tight')
plt.show()

np.savetxt(outfile,np.append(energy.reshape([num_e,1]),
    sqe.reshape([num_e,1]),axis=1),fmt='%3.4f')

