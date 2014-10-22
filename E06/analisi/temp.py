import csv
from math import *
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

	####  Qui vanno i dati 	####
dataG0 = np.genfromtxt("../dati/scope_0.csv", delimiter=',')

t0	= dataG0[2:,0]
t0_b=[]
for i in range(0,len(t0)-10):
	t0_b.append(t0[i])
V01	= dataG0[2:,1]
V01_b=[]
for i in range(0,len(V01)-10):
	V01_b.append((V01[i]+V01[i+1]+V01[i+2]+V01[i+3]+V01[i+4])+V01[i+5]+V01[i+6]+V01[i+7]+V01[i+8]+V01[i+9])
V02	= dataG0[2:,2]
V02_b=[]
for i in range(0,len(V02)-10):
	V02_b.append((V02[i]+V02[i+1]+V02[i+2]+V02[i+3]+V02[i+4])+V02[i+5]+V02[i+6]+V02[i+7]+V02[i+8]+V02[i+9])

dataG1 = np.genfromtxt("../dati/scope_1.csv", delimiter=',')

t1	= dataG1[2:,0]
t1_b=[]
for i in range(0,len(t1)-10):
	t1_b.append(200+t1[i])
V11	= dataG1[2:,1]
V11_b=[]
for i in range(0,len(V11)-10):
	V11_b.append((V11[i]+V11[i+1]+V11[i+2]+V11[i+3]+V11[i+4])+V11[i+5]+V11[i+6]+V11[i+7]+V11[i+8]+V11[i+9])
V12	= dataG1[2:,2]
V12_b=[]
for i in range(0,len(V12)-10):
	V12_b.append((V12[i]+V12[i+1]+V12[i+2]+V12[i+3]+V12[i+4])+V12[i+5]+V12[i+6]+V12[i+7]+V12[i+8]+V12[i+9])

	####	####	####	####

# Creo un grafico la dimensione è in pollici
fig1 = plt.figure(figsize=(14, 5.5))
# Titolo del grafico
fig1.suptitle("Temperatura in funzione del tempo", y=0.98, fontsize=15)

######
# GRAFICO 1
f1 = fig1.add_subplot(1, 1, 1)
#f1.set_xscale('log')

t01 = f1.errorbar(x=t0_b,
	y=V01_b,
	fmt='-', c='black')

t02 = f1.errorbar(x=t0_b,
	y=V02_b,
	fmt='-', c='green')

t11 = f1.errorbar(x=t1_b,
	y=V11_b,
	fmt='-', c='black')

t12 = f1.errorbar(x=t1_b,
	y=V12_b,
	fmt='-', c='green')
    
f1.text(-12, 29, u'Temperatura [°C]', size=14, va='center', ha='center',rotation='90')
#f1.text(0, -1.67, r'Frequenza [$Hz$]', rotation='horizontal', ha='center', va='center', fontsize=15)
#f1.text(-11.2, 0, r'Gain [$dB$]', rotation='vertical',	ha='center', va='center', fontsize=15)

#f1.text(100, 38, 'G=101x', #r'$\nu_0$',
#	size=12, va='center', ha='center')
#f1.text(100, 23, 'G=11x', size=12, va='center', ha='center')

f1.grid(True)
f1.set_ylim((24, 34))
#f1.set_xlim((-2.9,2.9))

f1.set_xlabel(u'Tempo [$s$]', labelpad=0, fontsize=14)

f1.legend((t01, t02), (r'Temperatura ambientale', r'Temperatura di soglia'), 'lower right', prop={'size': 13})
    
######

# questo imposta i bordi del grafico
fig1.subplots_adjust(left=0.0425, right=0.98, top=0.945, bottom=0.09, hspace=0.085, wspace=0.05)
# mostra grafico
plt.show()
