import csv
import sys
from math import *
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

	####  Qui vanno i dati 	####
dataG1 = np.genfromtxt("../dati/scope_7.csv", delimiter=',')

t1	= 1000*dataG1[2:,0]
V11	= dataG1[2:,1]
V12	= dataG1[2:,2]

dataG2 = np.genfromtxt("../dati/scope_8.csv", delimiter=',')

t2	= 1000*dataG2[2:,0]
V21	= dataG2[2:,1]
V22	= dataG2[2:,2]

	####	####	####	####

# Creo un grafico la dimensione è in pollici
fig1 = plt.figure(figsize=(8, 5.5))
# Titolo del grafico
fig1.suptitle("Stati di una porta NOT TTL Open Collector (74LS05)", y=0.97, fontsize=15)

######
# GRAFICO 1
f1 = fig1.add_subplot(1, 1, 1)
#f1.set_xscale('log')

g1 = f1.errorbar(x=t1, y=V11, fmt='-', c='black')
g2 = f1.errorbar(x=t1, y=V12, fmt='-', c='blue')
g3 = f1.errorbar(x=t2, y=V22, fmt='-', c='red')
    
##f1.text(-3.2, 0, u'Tensione [$V$]', size=14, va='center', ha='center',rotation='90')
#f1.text(0, -1.67, r'Frequenza [$Hz$]', rotation='horizontal', ha='center', va='center', fontsize=15)
#f1.text(-11.2, 0, r'Gain [$dB$]', rotation='vertical',	ha='center', va='center', fontsize=15)

#f1.text(100, 38, 'G=101x', #r'$\nu_0$',
#	size=12, va='center', ha='center')
#f1.text(100, 23, 'G=11x', size=12, va='center', ha='center')

f1.grid(True)
#f1.set_ylim((-400, 1000))
f1.set_xlim((-275,275))

f1.set_ylabel(u'd.d.p. [$V$]', labelpad=0, fontsize=14)
f1.set_xlabel(u'Tempo [$ms$]', labelpad=0, fontsize=14)

f1.legend((g1, g2, g3 ), (r'$V_{in}$', r'$V_{1}$', r'$V_{2}$'), 'upper right', prop={'size': 13})
    
######

# questo imposta i bordi del grafico
fig1.subplots_adjust(left=0.07	, right=0.98, top=0.93, bottom=0.09, hspace=0.085, wspace=0.05)
# mostra grafico
plt.show()
