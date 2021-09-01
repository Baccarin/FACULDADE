--------------------------------------------------------------------------

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 8))

selection1 = round((0+0+0+0+0)/5)/100
selection10 = round((0+0+0+0+0)/5)/100
selection100 = round((0+0+0+0+0)/5)/100
selection1000 = round((1+1+1+1+1)/5)/100
selection10000 = round((134+125+145+128+130)/5)/100
selection50000 = round((3727+3763+3345+3456+3655)/5)/100
selection100000 = round((12600+11526+13465+12546+11546)/5)/100
selection150000 = round((32500+31658+33264+31254+32653)/5)/100
selection250000 = round((38379+38269+38565+38455+38346)/5)/100
selection500000 = round(46000/100)

selectionY=np.array([selection1,selection10,selection100,selection1000,selection10000,selection50000,selection100000,selection150000,selection250000,selection500000])

x1 =  np.arange(len(selectionY))

plt.ylabel('Tempo em segundos')
plt.xlabel('Número de entradas')

plt.bar(x1,selectionY ,width=0.25, label = 'Selection Sort', color = 'y')


plt.legend()
plt.show()

fig.savefig('selectionplot.png')



