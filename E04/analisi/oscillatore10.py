import csv
from math import *
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

	####  Qui vanno i dati 	####
dataG1 = np.genfromtxt("../dati/scope_6.csv", delimiter=',')

t	=1000* dataG1[2:,0]
V_in	= dataG1[2:,1]
V_ou	= dataG1[2:,2]

	####	####	####	####

# Creo un grafico la dimensione è in pollici
fig1 = plt.figure(figsize=(8, 5.5))
# Titolo del grafico
fig1.suptitle(u'Risposta dell'"'"'oscillatore a rilassamento con $R=10k\Omega$', y=0.98, fontsize=15)

######
# GRAFICO 1
f1 = fig1.add_subplot(1, 1, 1)
#f1.set_xscale('log')

f1.text(-27.5, 6.9, '6.9', rotation='horizontal', ha='right', va='center', fontsize=12)
f1.axhline(y=6.9, xmin=0, xmax=1, lw=1, ls=':',c="0")
f1.text(-27.4, -6.6, r'$-$6.6', rotation='horizontal', ha='right', va='center', fontsize=12)
f1.axhline(y=-6.6, xmin=0, xmax=1, lw=1, ls=':',c="0")

g1 = f1.errorbar(x=t, #x=np.logspace(70,6E6,500),
	y=V_in,
	fmt='--', c='black')

g2 = f1.errorbar(x=t, #x=np.logspace(70,6E6,500),
	y=V_ou,
	fmt='-', c='green')

f1.grid(True)
f1.set_ylim((-15, 15))
f1.set_xlim((-2.8,2.8))

f1.text(-3, 0, u'Tensione [$V$]', size=14, va='center', ha='center',rotation='90')

f1.set_xlabel(u'Tempo [$m s$]', labelpad=0, fontsize=14)

f1.legend((g1, g2), (r'$V_C$', r'$V_{out}$'), 'lower left', prop={'size': 13})
    
######

# questo imposta i bordi del grafico
fig1.subplots_adjust(left=0.07, right=0.98, top=0.93, bottom=0.1, hspace=0.085, wspace=0.05)
# mostra grafico
plt.show()
