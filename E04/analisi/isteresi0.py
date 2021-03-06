import csv
from math import *
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

	####  Qui vanno i dati 	####
dataG1 = np.genfromtxt("../dati/scope_3.csv", delimiter=',')

t	= 1E3*dataG1[2:,0]
V_in	= dataG1[2:,1]
V_ou	= dataG1[2:,2]

	####	####	####	####

# Creo un grafico la dimensione è in pollici
fig1 = plt.figure(figsize=(8, 5.5))
# Titolo del grafico
fig1.suptitle("Ciclo di isteresi ", y=0.98, fontsize=15)

######
# GRAFICO 1
f1 = fig1.add_subplot(1, 1, 1)
#f1.set_xscale('log')

g1 = f1.errorbar(x=V_in, #x=np.logspace(70,6E6,500),
	y=V_ou,
	lw=0.5,	ls=':',
	marker='o', ms=2.5,
	c='black')

points = f1.plot([25.6, 2.6], [-8/2, 8/2], c='black', marker='o', ls='')

p10t = f1.text(25.6+0.5, -8/2+0.2/2, r'$P_{10\%}$', rotation='horizontal',
	ha='left', va='bottom', fontsize=22)
p90t = f1.text(2.6+0.5, 8/2+0.2/2, r'$P_{90\%}$', rotation='horizontal',
	ha='left', va='bottom', fontsize=22)

f1.text(-1.19, 2, u'$V_{out} $[$V$]', size=14, va='center', ha='center',rotation='90')    
#f1.set_ylabel(u'$V_{out} $[$V$]', labelpad=0, fontsize=14)
#f1.text(0, -1.67, r'Frequenza [$Hz$]', rotation='horizontal', ha='center', va='center', fontsize=15)
#f1.text(-11.2, 0, r'Gain [$dB$]', rotation='vertical',	ha='center', va='center', fontsize=15)

#f1.text(100, 38, 'G=101x', #r'$\nu_0$',
#	size=12, va='center', ha='center')
#f1.text(100, 23, 'G=11x', size=12, va='center', ha='center')

f1.grid(True)
f1.set_ylim((-1.2, 5.2))
f1.set_xlim((-1.1,1.1))

f1.set_xlabel(u'$V_{in} $[$V$]', labelpad=0, fontsize=14)

#f1.legend((g1,), (r'$V_{in}$',), 'lower left', prop={'size': 13})
    
######

# questo imposta i bordi del grafico
fig1.subplots_adjust(left=0.065, right=0.98, top=0.945, bottom=0.1, hspace=0.085, wspace=0.05)
# mostra grafico
plt.show()
