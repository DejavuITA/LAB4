import csv
import sys
from math import *
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

if len(sys.argv)==1:
	sys.exit()

	####  Qui vanno i dati 	####
dataG1 = np.genfromtxt("../dati/Dati2/scope_{}.csv".format(sys.argv[1]), delimiter=',')

t	= dataG1[2:,0]
V1	= dataG1[2:,1]
V2	= dataG1[2:,2]

	####	####	####	####

# Creo un grafico la dimensione è in pollici
fig1 = plt.figure(figsize=(8, 5.5))
# Titolo del grafico
fig1.suptitle("Risposta della porta", y=0.975, fontsize=15)

######
# GRAFICO 1
f1 = fig1.add_subplot(1, 1, 1)
#f1.set_xscale('log')

g1 = f1.errorbar(x=V1,	y=V2,	ls='', marker='.', c='black')
    
#f1.text(-3.2, 0, u'Tensione [$V$]', size=14, va='center', ha='center',rotation='90')
#f1.text(0, -1.67, r'Frequenza [$Hz$]', rotation='horizontal', ha='center', va='center', fontsize=15)
#f1.text(-11.2, 0, r'Gain [$dB$]', rotation='vertical',	ha='center', va='center', fontsize=15)

f1.grid(True)
#f1.set_ylim((-400, 1000))
f1.set_xlim((-0.5,5.5))

f1.set_ylabel(u'd.d.p. in uscita [$V$]', labelpad=0, fontsize=14)
f1.set_xlabel(u'd.d.p. in entrata [$V$]', labelpad=0, fontsize=14)

#f1.legend((g1, ), (r'$V_1$', ), 'upper right', prop={'size': 13})
    
######

# questo imposta i bordi del grafico
fig1.subplots_adjust(left=0.07, right=0.98, top=0.935, bottom=0.10, hspace=0.085, wspace=0.05)
# mostra grafico
plt.show()
