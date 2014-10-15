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

dataG1_1 = np.genfromtxt("../dati/scope_1.csv", delimiter=',')

t_1	=1000* dataG1_1[2:,0]
V_in_1	= dataG1_1[2:,1]
V_ou_1	= dataG1_1[2:,2]

	####	####	####	####

# Creo un grafico la dimensione è in pollici
fig1 = plt.figure(figsize=(8*2, 5.5))
# Titolo del grafico
fig1.suptitle("Risposta del raddrizzatore a mezz'onda", y=0.97, fontsize=15)

######
# GRAFICO 1
f1 = fig1.add_subplot(1, 2, 1)

g1 = f1.errorbar(x=V_in,
	y=V_ou,
	fmt='.:', c='black')

linea = f1.errorbar(
	x=np.arange(0, 0.5, 0.01),
	y=np.arange(0, 0.5, 0.01),
	fmt='-', c='r')
    
f1.text(-0.485, 0.6/2-0.05, u'$V_{OUT}$ [$V$]', size=14, va='center', ha='center',rotation='90')

f1.grid(True)
f1.set_ylim((-0.05, 0.55))
f1.set_xlim((-0.43, 0.53))

f1.set_xlabel(u'$V_{in} $[$V$]', labelpad=0, fontsize=14)

# GRAFICO 2
f5 = fig1.add_subplot(1, 2, 2)

g5 = f5.errorbar(x=V_in_1, #x=np.logspace(70,6E6,500),
	y=V_ou_1,
	fmt='.:', c='black')

linea5 = f5.errorbar(
	x=np.arange(0, 0.5, 0.01),
	y=0.3+np.arange(0, 0.5, 0.01),
	fmt='-', c='r')
    
f5.text(-0.61, -6, u'$V_A$ [$V$]', size=14, va='center', ha='center',rotation='90')

f5.grid(True)
f5.set_ylim((-13.5, 1.5))
f5.set_xlim((-0.55, 0.55))

f5.set_xlabel(u'$V_{in} $[$V$]', labelpad=0, fontsize=14)
    
######

# questo imposta i bordi del grafico
fig1.subplots_adjust(left=0.04, right=0.98, top=0.93, bottom=0.095, hspace=0.08, wspace=0.08)
# mostra grafico
plt.show()
