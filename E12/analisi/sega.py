import csv
import sys
from math import *
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

	####  Qui vanno i dati 	####
dataG1 = np.genfromtxt("../dati/scope_5.csv", delimiter=',')

t	= dataG1[2:,0]
V_in	= dataG1[2:,1]

	####	####	####	####

# Creo un grafico la dimensione è in pollici
fig1 = plt.figure(figsize=(8, 5.5))
# Titolo del grafico
fig1.suptitle("Dente di sega", y=0.97, fontsize=15)

######
# GRAFICO 1
f1 = fig1.add_subplot(1, 1, 1)

g1 = f1.errorbar(x=t, y=V_in, fmt='-', c='black')

f1.grid(True)
f1.set_ylim((-4.5, 0.5))
#f1.set_xlim((-1.8,1.8))

f1.set_ylabel(u'd.d.p. [$mV$]', labelpad=0, fontsize=14)
f1.set_xlabel(u'Tempo [$s$]', labelpad=0, fontsize=14)

f1.legend((g1, ), (r'$V_{out}$', ), 'upper right', prop={'size': 13})
    
######

# questo imposta i bordi del grafico
fig1.subplots_adjust(left=0.06, right=0.98, top=0.93, bottom=0.09, hspace=0.085, wspace=0.05)
# mostra grafico
plt.show()
