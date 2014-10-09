import csv
from math import *
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

	####  Qui vanno i dati 	####
dataG1 = np.genfromtxt("../dati/scope_8.csv", delimiter=',')

t	=1000* dataG1[2:,0]
V_in	= 1000*dataG1[2:,1]

	####	####	####	####

# Creo un grafico la dimensione è in pollici
fig1 = plt.figure(figsize=(8*0.8, 0.8*5.5))
# Titolo del grafico
fig1.suptitle("Rumore dovuto alla luce al neon", y=0.97, fontsize=15)

######
# GRAFICO 1
f1 = fig1.add_subplot(1, 1, 1)
#f1.set_xscale('log')

g1 = f1.errorbar(x=t, #x=np.logspace(70,6E6,500),
	y=V_in,
	fmt='-', c='red')

#g2 = f1.errorbar(x=t, #x=np.logspace(70,6E6,500),
	#y=V_in,
	#fmt='-', c='green')
    
#f1.set_ylabel(u'Tensione [$V$]', labelpad=0, fontsize=14)
#f1.text(0, -1.67, r'Frequenza [$Hz$]', rotation='horizontal', ha='center', va='center', fontsize=15)
#f1.text(-11.2, 0, r'Gain [$dB$]', rotation='vertical',	ha='center', va='center', fontsize=15)

#f1.text(100, 38, 'G=101x', #r'$\nu_0$',
#	size=12, va='center', ha='center')
#f1.text(100, 23, 'G=11x', size=12, va='center', ha='center')

f1.grid(True)


f1.text(-63.7, 0, u'Tensione [$mV$]', size=14, va='center', ha='center',rotation='90')

f1.set_ylim((-160, 160))
f1.set_xlim((-55,55))

f1.set_xlabel(u'Tempo [$m s$]', labelpad=0, fontsize=14)

#f1.legend((g1,), (r'$$',), 'lower left', prop={'size': 13})
    
######

# questo imposta i bordi del grafico
fig1.subplots_adjust(left=0.105, right=0.98, top=0.92, bottom=0.115, hspace=0.085, wspace=0.05)
# mostra grafico
plt.show()
