import csv
from math import *
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

	####  Qui vanno i dati 	####
dataG1 = np.genfromtxt("../dati/scope_1.csv", delimiter=',')

t	=1000* dataG1[2:,0]
V_in	= dataG1[2:,1]
V_ou	= dataG1[2:,2]

	####	####	####	####

# Creo un grafico la dimensione è in pollici
fig1 = plt.figure(figsize=(8, 5.5))
# Titolo del grafico
fig1.suptitle("Segnale del raddrizzatore in uscita dall'OPAMP", y=0.97, fontsize=15)

######
# GRAFICO 1
f1 = fig1.add_subplot(1, 1, 1)
#f1.set_xscale('log')

g1 = f1.errorbar(x=t, #x=np.logspace(70,6E6,500),
	y=V_in,
	fmt='--', c='black')

g2 = f1.errorbar(x=t, #x=np.logspace(70,6E6,500),
	y=V_ou,
	fmt='-', c='green')
    
f1.text(-33.5,-6, u'Tensione [$V$]', size=14, va='center', ha='center',rotation='90')

f1.grid(True)
f1.set_ylim((-13.8, 1.8))
#f1.set_xlim((-2.9,2.9))

f1.set_xlabel(u'Tempo [$m s$]', labelpad=0, fontsize=14)

f1.legend((g1, g2), (r'$V_{in}$', r'$V_{A}$'), 'center right', prop={'size': 13})
    
######

# questo imposta i bordi del grafico
fig1.subplots_adjust(left=0.08, right=0.98, top=0.93, bottom=0.1, hspace=0.085, wspace=0.05)
# mostra grafico
plt.show()
