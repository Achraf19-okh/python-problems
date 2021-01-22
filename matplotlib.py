import numpy as np
import pylab as pl

x = np.linspace(1,-5,-2)
y = np.linspace(1,-5,-2)

pl.xlabel('abscicess')
pl.plot(x,y,linewidth = 4,
        color='red',)
pl.show()
pl.close()

