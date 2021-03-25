import numpy as np
import h5py
from scipy.io import loadmat
import matplotlib.pyplot as plt

delta = 1e6

dat1 = '3.4.dat'
dat1 = np.loadtxt(dat1)
energy = dat1[:,0]
dat1 = dat1[:,1]

dat2 = '3.0.dat'
dat2 = np.loadtxt(dat2)[:,1]

dat3 = '2.6.dat'
dat3 = np.loadtxt(dat3)[:,1]

dat4 = '2.2.dat'
dat4 = np.loadtxt(dat4)[:,1]

dat5 = '1.8.dat'
dat5 = np.loadtxt(dat5)[:,1]

dat6 = '1.4.dat'
dat6 = np.loadtxt(dat6)[:,1]

dat7 = '1.0.dat'
dat7 = np.loadtxt(dat7)[:,1]



fig,ax = plt.subplots()

fig.set_size_inches(4,6,forward=True)

ax.plot(energy,dat1*5+6*delta,lw=1,color='k')
ax.plot(energy,dat2*5+5*delta,lw=1,color='k')
ax.plot(energy,dat3*4+4*delta,lw=1,color='k')
ax.plot(energy,dat4*4+3*delta,lw=1,color='k')
ax.plot(energy,dat5*1.5+2*delta,lw=1,color='k')
ax.plot(energy,dat6*1.5+1*delta,lw=1,color='k')
ax.plot(energy,dat7+0*delta,lw=1,color='k')



for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(1.5)
ax.minorticks_on()
ax.tick_params(which='both',width=1,labelsize='large')
ax.tick_params(which='major',length=5)
ax.tick_params(which='minor',length=2)
ax.set_yticklabels([])
ax.axis([0,50,-0.5e6,7e6])

ax.set_ylabel('S(|Q|,w)',labelpad=4.0,fontweight='normal',fontsize='large')
ax.set_xlabel('Energy (meV)',labelpad=2.0,fontweight='normal',fontsize='large')
 
ax.annotate(r"$\left| Q \right|$=3.4 (1/A)",xy=(0.73,0.9),
        xycoords="axes fraction",color='k',fontsize='small')
ax.annotate(r"$\left| Q \right|$=3.0 (1/A)",xy=(0.73,0.77),
        xycoords="axes fraction",color='k',fontsize='small')
ax.annotate(r"$\left| Q \right|$=2.6 (1/A)",xy=(0.73,0.64),
        xycoords="axes fraction",color='k',fontsize='small')
ax.annotate(r"$\left| Q \right|$=2.2 (1/A)",xy=(0.73,0.51),
        xycoords="axes fraction",color='k',fontsize='small')
ax.annotate(r"$\left| Q \right|$=1.8 (1/A)",xy=(0.73,0.375),
        xycoords="axes fraction",color='k',fontsize='small')
ax.annotate(r"$\left| Q \right|$=1.4 (1/A)",xy=(0.73,0.24),
        xycoords="axes fraction",color='k',fontsize='small')
ax.annotate(r"$\left| Q \right|$=1.0 (1/A)",xy=(0.73,0.1),
        xycoords="axes fraction",color='k',fontsize='small')


plt.savefig('aluminum_powder_vs_ref.pdf',format='pdf',dpi=150,bbox_inches='tight')
plt.show()


