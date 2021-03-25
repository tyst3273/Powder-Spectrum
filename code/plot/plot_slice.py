import numpy as np
import h5py
from scipy.io import loadmat
import matplotlib.pyplot as plt

Q_max = 11.2

filename = 'out_0067.mat'
with h5py.File(filename,'r') as f:
    sqe = np.nan_to_num(f['sqe'],nan=1e-6)
    energy = np.copy(f['energy'])[0,:]

num_Q = sqe.shape[1]
sqe = np.sum(sqe,axis=0)/num_Q

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

plt.savefig('aluminum_powder_spectrum_slice.pdf',format='pdf',dpi=150,bbox_inches='tight')
plt.show()

