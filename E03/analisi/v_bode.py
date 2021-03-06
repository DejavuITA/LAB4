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

Ax = log10(20E3)
Bx = log10(100E3)
Ay = 20*log10(9.07/0.199)
By = 20*log10(1.8/0.2)
m= (By-Ay)/(Bx-Ax)

	####	####	####	####

# Creo un grafico la dimensione è in pollici
fig1 = plt.figure(figsize=(8, 8))
# Titolo del grafico
fig1.suptitle("Risposta in frequenza dell'opamp µA741", y=0.985, fontsize=15)

######
# GRAFICO 1
f1 = fig1.add_subplot(2, 1, 1)


f1.set_xscale('log')

slope = f1.errorbar(x=np.logspace(0,7,num=500),
			y=0.43*m*np.log(np.logspace(0,7,num=500))+120,
	fmt='--', c='0.5')
f1.text(140000, 34, u'approx slope:', size=13, va='center', ha='center')
f1.text(140000, 32, u'$-20\,dB/decade$', size=13, va='center', ha='center')
f1.text(140000, 30, u'$-6\,dB/ottava$', size=13, va='center', ha='center')

A3=185900;
b3=1/11;
w03=5.9;

teo_db10 = f1.errorbar(x=np.logspace(0,7,num=500),
	y=20*np.log10(np.sqrt((A3*A3 * w03*w03)/((w03 + A3*b3*w03)*(w03 + A3*b3*w03) + np.logspace(0,7,num=500)*np.logspace(0,7,num=500)))),
	fmt='-', c='black', lw=1)

A4=173300;
b4=1/101;
w04=5.9;

teo_db100 = f1.errorbar(x=np.logspace(0,7,num=500),
	y=20*np.log10(np.sqrt((A4*A4 * w04*w04)/((w04 + A4*b4*w04)*(w04 + A4*b4*w04) + np.logspace(0,7,num=500)*np.logspace(0,7,num=500)))),
	fmt='-', c='green', lw=1)

db10 = f1.errorbar(x=f10, #x=np.logspace(70,6E6,500),
	y=20*np.log10(V_ou10/V_in10),
	marker='o', ms=3.9, ls='', c='black')

db100 = f1.errorbar(x=f100, #x=np.logspace(70,6E6,500),
	y=20*np.log10(V_ou100/V_in100),
	marker='o', ms=3.9, ls='', c='green')
    
f1.text(2.2, 25-6, u'Gain [$dB$]', rotation='vertical',	ha='center', va='center', fontsize=15)

f1.text(100, 38, 'G=101x', #r'$\nu_0$',
	size=12, va='center', ha='center')
f1.text(100, 23, 'G=11x', size=12, va='center', ha='center')

f1.grid(True)
f1.set_ylim((6,44))
#f1.set_xlim((80,4E6))
    
######
# GRAFICO 2
f2 = fig1.add_subplot(2, 1, 2, sharex=f1)
f2.set_xscale('log')

A1=170600;
b1=1/11;
w01=5.9;

teo_fase10 = f2.errorbar(x=np.logspace(0,7,num=500),
	y=180/pi*np.arctan(-np.logspace(0,7,num=500)/((1+A1*b1)*w01)),
	fmt='-', c='black', lw=1)

A2=177500;
b2=1/101;
w02=5.9;

teo_fase100 = f2.errorbar(x=np.logspace(0,7,num=500),
	y=180/pi*np.arctan(-np.logspace(0,7,num=500)/((1+A2*b2)*w02)),
	fmt='-', c='green', lw=1)

fase10 = f2.errorbar(x=f10, y=ph10, marker='o', ms=3.9, ls='', c='black')

fase100 = f2.errorbar(x=f100, y=ph100, marker='o', ms=3.9, ls='', c='green')

f2.text(2.2, -102/2+6, r'$\varphi \, \left[^\circ\right]$', rotation='vertical',	ha='center', va='center', fontsize=16, fontweight='bold')
f2.text(2.19, -102/2+6, r'$\varphi \, \left[^\circ\right]$', rotation='vertical',	ha='center', va='center', fontsize=16, fontweight='bold')
f2.set_xlabel(u'Frequency [$Hz$]', labelpad=0, fontsize=14)

f2.set_ylim((-96, 6))
f2.set_yticks(np.arange(-90, 1, 15))
f2.set_xlim((5,6E5))
plt.setp(f2.get_xticklabels(), visible=False)

f2.grid(True)
#f2.legend((fase10, fase100), ("Gain = 11x", "Gain = 101x"), 'upper right', prop={'size': 12})
    
######

# questo imposta i bordi del grafico
fig1.subplots_adjust(left=0.09, right=0.98, top=0.955, bottom=0.045, hspace=0.085, wspace=0.05)
# mostra grafico
plt.show()
