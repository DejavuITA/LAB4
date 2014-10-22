import csv
from math import *
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

	####  Qui vanno i dati 	####
dataG0 = np.genfromtxt("../dati/scope_0.csv", delimiter=',')

t0	= dataG0[2:,0]
V01	= dataG0[2:,1]
V02	= dataG0[2:,2]

dataG1 = np.genfromtxt("../dati/scope_1.csv", delimiter=',')

t1	= dataG1[2:,0]
V11	= dataG1[2:,1]
V12	= dataG1[2:,2]
t0_b=[]
V01_b=[]
V02_b=[]
for i in range(0,400):#len(t0)/5):
	t0_b.append(0.2*(t0[i]+t0[i+1]+t0[i+2]+t0[i+3]+t0[i+4]))
for i in range(0,400):#len(t0)/5):
	V01_b.append(0.2*(V01[i]+V01[i+1]+V01[i+2]+V01[i+3]+V01[i+4]))
for i in range(0,400):#len(t0)/5):
	V02_b.append(0.2*(V02[i]+V02[i+1]+V02[i+2]+V02[i+3]+V02[i+4]))
print(len(t0_b))
print(len(V01_b))
print(len(V02_b))


	####	####	####	####

# Creo un grafico la dimensione è in pollici
fig1 = plt.figure(figsize=(8, 5.5))
# Titolo del grafico
fig1.suptitle("Temperatura in funzione del tempo", y=0.97, fontsize=15)

######
# GRAFICO 1
f1 = fig1.add_subplot(1, 1, 1)
#f1.set_xscale('log')

t01 = f1.errorbar(x=t0, #x=np.logspace(70,6E6,500),
	y=10*V01,
	fmt='.', c='black')

t02 = f1.errorbar(x=t0, #x=np.logspace(70,6E6,500),
	y=10*V02,
	fmt='.', c='green')

t11 = f1.errorbar(x=t1+200, #x=np.logspace(70,6E6,500),
	y=10*V11,
	fmt='.', c='black')

t12 = f1.errorbar(x=t1+200, #x=np.logspace(70,6E6,500),
	y=10*V12,
	fmt='.', c='green')
    
f1.text(0, 30, u'Temperatura [°C]', size=14, va='center', ha='center',rotation='90')
#f1.text(0, -1.67, r'Frequenza [$Hz$]', rotation='horizontal', ha='center', va='center', fontsize=15)
#f1.text(-11.2, 0, r'Gain [$dB$]', rotation='vertical',	ha='center', va='center', fontsize=15)

#f1.text(100, 38, 'G=101x', #r'$\nu_0$',
#	size=12, va='center', ha='center')
#f1.text(100, 23, 'G=11x', size=12, va='center', ha='center')

f1.grid(True)
#f1.set_ylim((-11, 11))
#f1.set_xlim((-2.9,2.9))

f1.set_xlabel(u'Tempo [$s$]', labelpad=0, fontsize=14)

f1.legend((t01, t02), (r'$V_{noise}$', r'$V_{out}$'), 'lower right', prop={'size': 13})
    
######

# questo imposta i bordi del grafico
fig1.subplots_adjust(left=0.06, right=0.98, top=0.93, bottom=0.09, hspace=0.085, wspace=0.05)
# mostra grafico
plt.show()
