import numpy as np
import h5py
from scipy.io import loadmat
import matplotlib.pyplot as plt

n_files = 220
Q_max = 11.2

filename = 'out_0001.mat'
with h5py.File(filename,'r') as f:
    sqe = np.nan_to_num(f['sqe'],nan=1e-6)
    energy = np.copy(f['energy'])[0,:]

num_Q = sqe.shape[1]
sqe_all = np.zeros((energy.shape[0],n_files))
sqe_all[:,0] = np.sum(sqe,axis=0)/num_Q


for i in range(1,n_files):
    filename = f'out_{i+1:04d}.mat'
    print(filename)
    with h5py.File(filename,'r') as f:
        sqe = np.nan_to_num(f['sqe'],nan=1e-6)

    num_Q = sqe.shape[1]
    sqe_all[:,i] = np.sum(sqe,axis=0)/num_Q


fig,ax = plt.subplots()
fig.set_size_inches(6,3,forward=True)

im = ax.imshow(np.log(sqe_all),origin='lower',aspect='auto',
        cmap='jet',interpolation='none',extent=[0,Q_max,0,energy.max()],
        vmin=-10,vmax=8)
fig.colorbar(im,ax=ax,extend='both')

for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(1.5)
ax.minorticks_on()
ax.tick_params(which='both',width=1,labelsize='large')
ax.tick_params(which='major',length=5)
ax.tick_params(which='minor',length=2)
ax.axis([0,Q_max,0,65])

ax.set_xlabel('|Q| (1/A)',labelpad=4.0,fontweight='normal',fontsize='large')
ax.set_ylabel('Energy (meV)',labelpad=2.0,fontweight='normal',fontsize='large')

plt.savefig('aluminum_powder_spectrum.pdf',format='pdf',dpi=150,bbox_inches='tight')
plt.show()

