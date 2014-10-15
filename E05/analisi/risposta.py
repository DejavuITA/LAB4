import csv
from math import *
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

	####  Qui vanno i dati 	####
dataG1 = np.genfromtxt("../dati/scope_4.csv", delimiter=',')

t	=1000* dataG1[2:,0]
V_in	= dataG1[2:,1]
V_ou	= dataG1[2:,2]

	####	####	####	####

# Creo un grafico la dimensione è in pollici
fig1 = plt.figure(figsize=(8, 5.5))
# Titolo del grafico
fig1.suptitle("Risposta del raddrizzatore a mezz'onda", y=0.97, fontsize=15)

######
# GRAFICO 1
f1 = fig1.add_subplot(1, 1, 1)
#f1.set_xscale('log')

g1 = f1.errorbar(x=V_in, #x=np.logspace(70,6E6,500),
	y=V_ou
,
	fmt='.:', c='black')

#g2 = f1.errorbar(x=t, #x=np.logspace(70,6E6,500),
	#y=V_ou,
	#fmt='-', c='green')
    
f1.text(-0.445, 0.2, u'Tensione [$V$]', size=14, va='center', ha='center',rotation='90')
#f1.text(0, -1.67, r'Frequenza [$Hz$]', rotation='horizontal', ha='center', va='center', fontsize=15)
#f1.text(-11.2, 0, r'Gain [$dB$]', rotation='vertical',	ha='center', va='center', fontsize=15)

#f1.text(100, 38, 'G=101x', #r'$\nu_0$',
#	size=12, va='center', ha='center')
#f1.text(100, 23, 'G=11x', size=12, va='center', ha='center')

f1.grid(True)
#f1.set_ylim((-0.5, 2.5))
#f1.set_xlim((1.6,2.3))

f1.set_xlabel(u'$V_{in} $[$V$]', labelpad=0, fontsize=14)

#f1.legend((g1,), (r'$V_{in}$',), 'lower left', prop={'size': 13})
    
######

# questo imposta i bordi del grafico
fig1.subplots_adjust(left=0.07, right=0.98, top=0.93, bottom=0.11, hspace=0.085, wspace=0.05)
# mostra grafico
plt.show()
