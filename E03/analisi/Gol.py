import csv
from math import *
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

	####  Qui vanno i dati 	####
dataG1 = np.genfromtxt("../dati/4.1.csv", delimiter=',')

f_1	= dataG1[3:,0]
V_A1	= dataG1[3:,1]
V_out1	= dataG1[3:,2]

dataG2 = np.genfromtxt("../dati/4.2.csv", delimiter=',')

f_2	= dataG2[3:,0]#[2:7,0]
V_A2	= dataG2[3:,1]#[2:7,1]
V_out2	= dataG2[3:,2]#[2:7,2]


dataG3 = np.genfromtxt("../dati/4.3.csv", delimiter=',')

f_3	= dataG3[3:,0]#[2:7,0]
V_A3	= dataG3[3:,1]#[2:7,1]
V_out3	= dataG3[3:,2]#[2:7,2]


dataG4 = np.genfromtxt("../dati/4.4.csv", delimiter=',')

f_4	= dataG4[3:,0]#[2:7,0]
V_A4	= dataG4[3:,1]#[2:7,1]
V_out4	= dataG4[3:,2]#[2:7,2]


dataG5 = np.genfromtxt("../dati/4.5.csv", delimiter=',')

f_5	= dataG5[3:,0]#[2:7,0]
V_A5	= dataG5[3:,1]#[2:7,1]
V_out5	= dataG5[3:,2]#[2:7,2]

	####	####	####	####

# Creo un grafico la dimensione è in pollici
fig1 = plt.figure(figsize=(8, 8))
# Titolo del grafico
fig1.suptitle("Gain open-loop", y=0.985, fontsize=15)

######
# GRAFICO 1
f1 = fig1.add_subplot(1, 1, 1)
f1.set_xscale('log')

db10 = f1.errorbar(x=f_1, #x=np.logspace(70,6E6,500),
	y=20*np.log10(V_out1/V_A1*1001),
	fmt='.:', c='black')

db100 = f1.errorbar(x=f_2, #x=np.logspace(70,6E6,500),
	y=20*np.log10(V_out2/V_A2),
	fmt='.:', c='green')
    
f1.set_ylabel(u'Gain [$dB$]', labelpad=0, fontsize=14)
#f1.text(0, -1.67, r'Frequenza [$Hz$]', rotation='horizontal', ha='center', va='center', fontsize=15)
#f1.text(-11.2, 0, r'Gain [$dB$]', rotation='vertical',	ha='center', va='center', fontsize=15)

#f1.text(100, 38, 'G=101x', #r'$\nu_0$',
#	size=12, va='center', ha='center')
#f1.text(100, 23, 'G=11x', size=12, va='center', ha='center')

f1.grid(True)
f1.set_ylim((-10, 120))
f1.set_xlim((1, 2E6))

f1.set_xlabel(u'Frequenza [$Hz$]', labelpad=0, fontsize=14)

#f1.legend((db10, db100), ("Gain = 11x", "Gain = 101x"), 'lower left', prop={'size': 12})
    
######

# questo imposta i bordi del grafico
fig1.subplots_adjust(left=0.07, right=0.98, top=0.93, bottom=0.11, hspace=0.085, wspace=0.05)
# mostra grafico
plt.show()