import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 8))

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

selection1 = round((0+0+0+0+0)/5)/100
selection10 = round((0+0+0+0+0)/5)/100
selection100 = round((0+0+0+0+0)/5)/100
selection1000 = round((1+1+1+1+1)/5)/100
selection10000 = round((134+125+145+128+130)/5)/100
selection50000 = round((3727+3763+3345+3456+3655)/5)/100
selection100000 = round((12600+11526+13465+12546+11546)/5)/100
selection150000 = round((32500+31658+33264+31254+32653)/5)/100
selection250000 = round((38379+38259+38465+38445+38646)/5)/100
selection500000 = round(46000/100)

selectionY=np.array([selection1,selection10,selection100,selection1000,selection10000,selection50000,selection100000,selection150000,selection250000,selection500000])

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

x1 =  np.arange(len(insertionY))
x2 = [x + 0.25 for x in x1]
x3 = [x + 1.25 for x in x1]


plt.ylabel('Tempo em segundos')
plt.xlabel('Número de entradas')

plt.bar(x1,insertionY,width=0.25, label = 'Insertion', color = 'b')

plt.bar(x2,selectionY ,width=0.25, label = 'Selection', color = 'y')

plt.bar(x3,mergeY ,width=0.55, label = 'Merge', color = 'g')

plt.legend()
plt.show()


fig.savefig('barrastotaisplot.png')

