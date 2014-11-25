import csv
import sys
from math import *
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA

	####  Qui vanno i dati 	####
dataG1 = np.genfromtxt("../dati/scope_2.csv", delimiter=',')
dataG2 = np.genfromtxt("../dati/scope_3.csv", delimiter=',') #o 5, o 7
#dataG3 = np.genfromtxt("../dati/scope_3.csv", delimiter=',')
r=10
T=1E3

t1	= T*dataG1[2:,0]
V1	= dataG1[2:,1]

t2	= T*dataG1[2:,0]
V2	= dataG1[2:,2]

t3	= T*dataG2[2:,0]+640
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

g1 = f1.errorbar(	x=t1,	y=V1,		fmt='-', c='black')

f1.grid(True)
#f1.set_ylim((-14, 14))
#f1.set_xlim((-87,70))

f1.text(-97, 0, u'd.d.p. [$V$]', size=14, va='center', ha='center',rotation='90')
f1.set_xlabel(u'Tempo [$ms$]', labelpad=0, fontsize=14)

f1.legend((g1, ), (r'$V_{gen}$', ), 'lower left', prop={'size': 13})

######
# GRAFICO 2
#f2 = fig1.add_subplot(1, 3, 2)
f2 = host_subplot(312, axes_class=AA.Axes)

g2 = f2.errorbar(	x=t2,	y=V2,		fmt='-', c='black')

f2.grid(True)
#f2.set_ylim((-14, 14))
#f2.set_xlim((-1.8,1.8))

f2.set_xlabel(u'Tempo [$ms$]', labelpad=0, fontsize=14)

f2.legend((g2, ), (r'$V_{A}$', ), 'lower left', prop={'size': 13})
    
######
# GRAFICO 3
#f3 = fig1.add_subplot(1, 3, 3)
f3 = host_subplot(313, axes_class=AA.Axes)

g3 = f3.errorbar(	x=t3-640,	y=V3,		fmt='-', c='black')

f3.grid(True)
f3b = f3.twin()
f3b.axis["top"].major_ticklabels.set_visible(False)
f3b.axis["right"].major_ticklabels.set_visible(False)
#f3.set_ylim((-14, 14))
#f3.set_xlim((-27,87))

f3.text(94.5, 0, u'd.d.p. [$V$]', size=14, va='center', ha='center',rotation='-90')
f3.set_xlabel(u'Tempo [$ms$]', labelpad=0, fontsize=14)

f3.legend((g3, ), (r'$V_{B}$', ), 'lower left', prop={'size': 13})
    
######

# questo imposta i bordi del grafico
fig1.subplots_adjust(left=0.04, right=0.96, top=0.93, bottom=0.09, hspace=0.05, wspace=0.03)
# mostra grafico
plt.show()
