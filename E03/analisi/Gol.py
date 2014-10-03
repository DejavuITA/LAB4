import csv
from math import *
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

	####  Qui vanno i dati 	####
R=100000

dataG1 = np.genfromtxt("../dati/4.1.csv", delimiter=',')

f_1	= dataG1[3:,0]
VA_1	= dataG1[3:,1]
Vout_1	= dataG1[3:,2]
R_1 = 5

dataG2 = np.genfromtxt("../dati/4.2.csv", delimiter=',')

f_2	= dataG2[3:,0]#[2:7,0]
VA_2	= dataG2[3:,1]#[2:7,1]
Vout_2	= dataG2[3:,2]#[2:7,2]
R_2 = 10

dataG3 = np.genfromtxt("../dati/4.3.csv", delimiter=',')

f_3	= dataG3[3:,0]#[2:7,0]
VA_3	= dataG3[3:,1]#[2:7,1]
Vout_3	= dataG3[3:,2]#[2:7,2]
R_3 = 100

dataG4 = np.genfromtxt("../dati/4.4.csv", delimiter=',')

f_4	= dataG4[3:,0]#[2:7,0]
VA_4	= dataG4[3:,1]#[2:7,1]
Vout_4	= dataG4[3:,2]#[2:7,2]
R_4 = 1000

dataG5 = np.genfromtxt("../dati/4.2_old.csv", delimiter=',')

f_5	= dataG5[3:,0]#[2:7,0]
VA_5	= dataG5[3:,1]#[2:7,1]
Vout_5	= dataG5[3:,2]#[2:7,2]
#R_5 = \infty

	####	####	####	####

# Creo un grafico la dimensione è in pollici
fig1 = plt.figure(figsize=(8, 5))
# Titolo del grafico
fig1.suptitle("Gain open-loop", y=0.985, fontsize=15)

######
# GRAFICO 1
f1 = fig1.add_subplot(1, 1, 1)
f1.set_xscale('log')

#x=np.logspace(70,6E6,500),
ohmE0 = f1.errorbar(x=f_1, y=20*np.log10(Vout_1/VA_1*(R+R_1)/R_1),
		c='0.5', fmt='s', ms=4, ls='--', lw='1')
ohmE1 = f1.errorbar(x=f_2, y=20*np.log10(Vout_2/VA_2*(R+R_2)/R_2),
		c='r', fmt='^', ms=5, ls='--', lw='1')
ohmE2 = f1.errorbar(x=f_3, y=20*np.log10(Vout_3/VA_3*(R+R_3)/R_3),
		c='b', marker='o', ms=5, ls='--', lw='1')
ohmE3 = f1.errorbar(x=f_4, y=20*np.log10(Vout_4/VA_4*(R+R_4)/R_4),
		c='y', marker='d', ms=5, ls='--', lw='1')
infty = f1.errorbar(x=f_5, y=20*np.log10(Vout_5/VA_5),
		c='g', marker='*', ls='--', lw='1')
    
#f1.text(0, -1.67, r'Frequenza [$Hz$]', rotation='horizontal', ha='center', va='center', fontsize=15)


#f1.text(100, 38, 'G=101x', #r'$\nu_0$',
#	size=12, va='center', ha='center')
#f1.text(100, 23, 'G=11x', size=12, va='center', ha='center')

f1.grid(True)
f1.set_ylim((-10, 125))
f1.set_xlim((0.5, 2E6))

f1.set_ylabel(u'Gain [$dB$]', labelpad=0, fontsize=14)
#f1.text(10, 115/2-10, r'Gain [$dB$]', rotation='vertical',	ha='center', va='center', fontsize=15)
f1.set_xlabel(u'Frequenza [$Hz$]', labelpad=-1, fontsize=14)

f1.legend((ohmE0, ohmE1, ohmE2, ohmE3, infty), (r'$R_4 = 5 \Omega$', r'$R_4 = 10 \Omega$', r'$R_4 = 100 \Omega$', r'$R_4 = 1000 \Omega$', r'$R_4 = \infty$'), 'upper right', prop={'size': 12})
    
######

# questo imposta i bordi del grafico
fig1.subplots_adjust(left=0.08, right=0.965, top=0.945, bottom=0.11)
# mostra grafico
plt.show()
#plt.savefig("gol.pdf")
