import csv
import sys
from math import *
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA

	####  Qui vanno i dati 	####
dataG1 = np.genfromtxt("../dati/scope_2_bis.csv", delimiter=',')
dataG2 = np.genfromtxt("../dati/scope_3_bis.csv", delimiter=',') #o 5, o 7
#dataG3 = np.genfromtxt("../dati/scope_3.csv", delimiter=',')
r=10
T=1E3

t1	= T*dataG1[2:,0]
V1	= dataG1[2:,1]

t2	= T*dataG1[2:,0]
V2	= dataG1[2:,2]

t3	= T*dataG2[2:,0]
V3	= dataG2[2:,2]

	####	####	####	####

# Creo un grafico la dimensione è in pollici
fig1 = plt.figure(figsize=(14, 5.5))
# Titolo del grafico
fig1.suptitle("Divisore di frequenze", y=0.97, fontsize=15)

######
# GRAFICO 1
#f1 = fig1.add_subplot(1, 3, 1)
f1 = host_subplot(311, axes_class=AA.Axes)

g1 = f1.errorbar(x=t1-20,	y=V1,	fmt='-', c='black')
g1 = f1.errorbar(x=t1,	y=V1,	fmt='-', c='black')
g1 = f1.errorbar(x=t1+20,	y=V1,	fmt='-', c='black')

f1.grid(True)
f1.set_ylim((-0.5, 5.5))
f1.set_xlim((-12.4,12.4))

f1.text(-97, 0, u'd.d.p. [$V$]', size=14, va='center', ha='center',rotation='90')
f1.set_xlabel(u'Tempo [$ms$]', labelpad=0, fontsize=14)

f1.legend((g1, ), (r'$V_{gen}$', ), 'upper left', prop={'size': 13})

######
# GRAFICO 2
#f2 = fig1.add_subplot(1, 3, 2)
f2 = host_subplot(312, axes_class=AA.Axes)

g2 = f2.errorbar(x=t2-20,	y=V2,	fmt='-', c='black')
g2 = f2.errorbar(x=t2,	y=V2,	fmt='-', c='black')
g2 = f2.errorbar(x=t2+20,	y=V2,	fmt='-', c='black')

f2.grid(True)
f2.set_ylim((-0.5, 5.5))
f2.set_xlim((-12.4,12.4))

f2.set_xlabel(u'Tempo [$ms$]', labelpad=0, fontsize=14)
f2.set_ylabel(u'd.d.p [$V$]', labelpad=0, fontsize=14)

f2.legend((g2, ), (r'$V_{A}$', ), 'upper left', prop={'size': 13})
    
######
# GRAFICO 3
#f3 = fig1.add_subplot(1, 3, 3)
f3 = host_subplot(313, axes_class=AA.Axes)

g3 = f3.errorbar(x=t3-20,	y=V3,	fmt='-', c='black')
g3 = f3.errorbar(x=t3,	y=V3,	fmt='-', c='black')
g3 = f3.errorbar(x=t3+20,	y=V3,	fmt='-', c='black')

f3.grid(True)
f3.axis["bottom"].major_ticklabels.set_visible(False)
f3.set_ylim((-0.5, 5.5))
f3.set_xlim((-12.4,12.4))

f3.text(94.5, 0, u'd.d.p. [$V$]', size=14, va='center', ha='center',rotation='-90')
f3.set_xlabel(u'Tempo [$ms$]', labelpad=0, fontsize=14)

f3.legend((g3, ), (r'$V_{B}$', ), 'upper left', prop={'size': 13})
    
######

# questo imposta i bordi del grafico
fig1.subplots_adjust(left=0.04, right=0.96, top=0.93, bottom=0.07, hspace=0.15, wspace=0.10)
# mostra grafico
plt.show()
