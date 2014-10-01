import csv
from math import *
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

	####  Qui vanno i dati 	####
dataG10 = np.genfromtxt("../dati/BW_G10.csv", delimiter=',')

f10	= dataG10[2:,0]
V_in10	= dataG10[2:,1]
V_ou10	= dataG10[2:,2]
ph10	= dataG10[2:,3]

dataG100 = np.genfromtxt("../dati/BW_G100.csv", delimiter=',')

f100	= dataG100[2:,0]
V_in100	= dataG100[2:,1]
V_ou100	= dataG100[2:,2]
ph100	= dataG100[2:,3]
	####	####	####	####

# Creo un grafico la dimensione è in pollici
fig1 = plt.figure(figsize=(8, 5.5))
# Titolo del grafico
fig1.suptitle("Risposta in frequenza dell'opamp µA741", y=0.97, fontsize=15)

######
# GRAFICO 1
f2 = fig1.add_subplot(1, 1, 1)
f2.set_xscale('log')

fase10 = f2.errorbar(x=f10, y=ph10, fmt='.:', c='black')

fase100 = f2.errorbar(x=f100, y=ph100, fmt='.:', c='green')

f2.set_ylabel(u'Fase [$^\circ$]', labelpad=0, fontsize=14)
f2.set_xlabel(u'Frequenza [$Hz$]', labelpad=0, fontsize=14)

f2.text(2E4, -37.5, 'G=101x', #r'$\nu_0$',
	size=12, va='center', ha='center')
f2.text(2E5, -37.5, 'G=11x', size=12, va='center', ha='center')

f2.set_ylim((-96, 6))
f2.set_yticks(np.arange(-90, 1, 15))
f2.set_xlim((5,6E5))

#plt.setp(f2.get_xticklabels(), visible=False)

f2.grid(True)
#f2.legend((fase10, fase100), ("Gain = 11x", "Gain = 101x"), 'lower left', prop={'size': 12})  
######

# questo imposta i bordi del grafico
fig1.subplots_adjust(left=0.09, right=0.98, top=0.93, bottom=0.11, hspace=0.085, wspace=0.05)
# mostra grafico
plt.show()
