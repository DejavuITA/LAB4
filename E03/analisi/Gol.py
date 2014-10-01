import csv
from math import *
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

	####  Qui vanno i dati 	####
dataG1 = np.genfromtxt("../dati/4.1.csv", delimiter=',')

f1	= dataG1[2:,0]
V_A1	= dataG1[2:,1]
V_out1	= dataG1[2:,2]

dataG2 = np.genfromtxt("../dati/4.2.csv", delimiter=',')

f2	= dataG2[2:,0]#[2:7,0]
V_A2	= dataG2[2:,1]#[2:7,1]
V_out2	= dataG2[2:,2]#[2:7,2]

	####	####	####	####

# Creo un grafico la dimensione è in pollici
fig1 = plt.figure(figsize=(8, 8))
# Titolo del grafico
fig1.suptitle("Gain open-loop", y=0.985, fontsize=15)

######
# GRAFICO 1
f1 = fig1.add_subplot(2, 1, 1)
f1.set_xscale('log')

db10 = f1.errorbar(x=f1, #x=np.logspace(70,6E6,500),
	y=20*np.log10(V_out1/V_A1*1001),
	fmt='.:', c='black')

db100 = f1.errorbar(x=f2, #x=np.logspace(70,6E6,500),
	y=20*np.log10(V_out2/V_A2),
	fmt='.:', c='green')
    
f1.set_ylabel(u'Gain [$dB$]', labelpad=0, fontsize=14)
#f1.text(0, -1.67, r'Frequenza [$Hz$]', rotation='horizontal', ha='center', va='center', fontsize=15)
#f1.text(-11.2, 0, r'Gain [$dB$]', rotation='vertical',	ha='center', va='center', fontsize=15)

f1.text(100, 38, 'G=101x', #r'$\nu_0$',
	size=12, va='center', ha='center')
f1.text(100, 23, 'G=11x', size=12, va='center', ha='center')

f1.grid(True)
#f1.set_ylim((-21, 21))
#f1.set_xlim((80,4E6))
    
######
# GRAFICO 2 - grafico R-Scarti
#f2 = fig1.add_subplot(2, 1, 2, sharex=f1)
#f2.set_xscale('log')

#fase10 = f2.errorbar(x=f10, y=ph10, fmt='.:', c='black')

#fase100 = f2.errorbar(x=f100, y=ph100, fmt='.:', c='green')

#f2.set_ylabel(u'Fase [$^\circ$]', labelpad=0, fontsize=14)
#f2.set_xlabel(u'Frequenza [$Hz$]', labelpad=0, fontsize=14)

#f2.set_ylim((-0, 190))
#f2.set_yticks(np.arange(0, 181, 45))
#f2.set_xlim((80,4E6))
#plt.setp(f2.get_xticklabels(), visible=False)

#f2.grid(True)
#f2.legend((fase10, fase100), ("Gain = 11x", "Gain = 101x"), 'upper right', #prop={'size': 12})
    
######

# questo imposta i bordi del grafico
fig1.subplots_adjust(left=0.09, right=0.98, top=0.955, bottom=0.045, hspace=0.085, wspace=0.05)
# mostra grafico
plt.show()