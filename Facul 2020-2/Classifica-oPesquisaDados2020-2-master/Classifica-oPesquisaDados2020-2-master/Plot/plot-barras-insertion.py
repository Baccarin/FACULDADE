import matplotlib.pyplot as plt
import numpy as np

insertion1 = round((0+0+0+0+0)/5)/100
insertion10 = round((0+0+0+0+0)/5)/100
insertion100 = round((0+0+0+0+0)/5)/100
insertion1000 = round((0+0+0+0+0)/5)/100
insertion10000 = round((108+100+94+115+109)/5)/100
insertion50000 = round((1546+1564+1256+1548+1499)/5)/100
insertion100000 = round((6978+7631+7299+7456+7591)/5)/100
insertion150000 = round((7889+7954+8215+8125+7959)/5)/100
insertion250000 = round((12451+13652+10956+11214+11102)/5)/100
insertion500000 = round((31254+32653+33652+36524+37854)/5)/100

insertionY=np.array([insertion1,insertion10,insertion100,insertion1000,insertion10000,insertion50000,insertion100000,insertion150000,insertion250000,insertion500000])

x1 =  np.arange(len(insertionY))

plt.ylabel('Tempo em segundos')
plt.xlabel('Número de entradas')

plt.bar(x1,insertionY,width=0.25, label = 'Insertion', color = 'b')


plt.legend()
plt.show()

