import matplotlib.pyplot as plt
import numpy as np

merge1 = round((0+0+0+0+0)/5)/100
merge10 = round((0+0+0+0+0)/5)/100
merge100 = round((0+0+0+0+0)/5)/100
merge1000 = round((0+0+0+0+0)/5)/100
merge10000 = round((2+3+1+4+2)/5)/100
merge50000 = round((16+15+17+16+16)/5)/100
merge100000 = round((28+29+27+28+28)/5)/100
merge150000 = round((56+44+44+52+62)/5)/100
merge250000 = round((89+84+82+85+85)/5)/100
merge500000 = round((190+150+151+160+177)/5)/100

mergeY=np.array([merge1,merge10,merge100,merge1000,merge10000,merge50000,merge100000,merge150000,merge250000,merge500000])

x1 =  np.arange(len(mergeY))

plt.ylabel('Tempo em segundos')
plt.xlabel('Número de entradas')

plt.bar(x1,mergeY ,width=0.25, label = 'Produto C', color = 'g')

plt.legend()
plt.show()

