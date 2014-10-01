import csv
from math import *
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

# Qui vanno i dati
dati = np.genfromtxt("../dati/bode.csv", delimiter=',')

V1 = 2
V2 = dati[1:,0]
PHI = dati[1:,2]
FREQ = dati[1:,1]

# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(8, 8))
# Titolo del grafico
f1.suptitle("Amplificatore invertente", y=0.985, fontsize=15)

######
# GRAFICO 1
ax1 = f1.add_subplot(2, 1, 1)
ax1.set_xscale('log')

db = ax1.errorbar(x=FREQ, #x=np.logspace(70,6E6,500),
	y=20*np.log10(V2/V1),
	fmt='.:', c='black')
#gain = ax1.errorbar(x=FREQ,
#	y=V2/V1,
#	fmt='.', c='black')
    
ax1.set_ylabel(u'Guadagno [$dB$]', labelpad=0, fontsize=14)
#ax1.set_ylabel(u'Guadagno', labelpad=2, fontsize=14)

#ax1.text(1/(2*pi*(L*C)**(0.5))+1000, -50+1.5, r'$\nu_0$', size=15, va='center')

ax1.grid(True)
ax1.set_ylim((-21, 21))
ax1.set_xlim((80,4E6))
    
######
# GRAFICO 2 - grafico R-Scarti
ax2 = f1.add_subplot(2, 1, 2, sharex=ax1)
ax2.set_xscale('log')
fase = ax2.errorbar(x=FREQ, y=PHI,
    fmt='.:', c='black')

ax2.set_ylabel(u'Fase [$^\circ$]', labelpad=0, fontsize=14)
ax2.set_xlabel(u'Frequenza [$Hz$]', labelpad=0, fontsize=14)

ax2.set_ylim((-0, 190))
ax2.set_yticks(np.arange(0, 181, 45))
ax2.set_xlim((80,4E6))
plt.setp(ax2.get_xticklabels(), visible=False)

ax2.grid(True)
ax2.legend((fase, ), ("Dati sperimentali", ), 'upper right', prop={'size': 12})
    
######

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.09, right=0.98, top=0.955, bottom=0.045, hspace=0.085, wspace=0.05)
# mostra grafico
plt.show()
