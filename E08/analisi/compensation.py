import csv
import sys
from math import *
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

	####  Qui vanno i dati 	####
dataG1 = np.genfromtxt("../dati/scope_11.csv", delimiter=',')
r=100
T=1E3
t1	= T*dataG1[2:,0]
#t1b=[]
#for i in range(0,len(t1)):
#	if i%r==0:
#		t1b.append(t1[i])
#t1c=[]
#for i in range(0,len(t1)-r):
#	t1c.append(t1[i])
V1	= dataG1[2:,1]
#V1b=[]
#for i in range(0,len(V1)):
#	if i%r==0:
#		V1b.append(V1[i])
#V1c=[]
#for i in range(0,len(V1)-r):
#	a=0	
#	for j in range(1,r):
#		a=a+V1[i+j]
#	a=a/r
#	V1c.append(a)

dataG2 = np.genfromtxt("../dati/scope_13.csv", delimiter=',')

t2	= T*dataG2[2:,0]
V2	= dataG2[2:,1]

dataG3 = np.genfromtxt("../dati/scope_14.csv", delimiter=',')

t3	= T*dataG3[2:,0]
V3	= dataG3[2:,1]

t4=[]
for i in range(0,len(V2)-3):
	t4.append(t2[i])
V4=[]
for i in range(0,len(V2)-3):
	a=V3[i+3]*1.7/10-V2[i]*0.7
	V4.append(a)

	####	####	####	####

# Creo un grafico la dimensione è in pollici
fig1 = plt.figure(figsize=(8, 5.5))
# Titolo del grafico
fig1.suptitle("Pole-Zero compensation", y=0.97, fontsize=15)

######
# GRAFICO 1
f1 = fig1.add_subplot(1, 1, 1)
#f1.set_xscale('log')

#g1 = f1.errorbar(	x=t1b,	y=V1b,		fmt='-', c='black')
#g1c = f1.errorbar(	x=t1c,	y=V1c,		fmt='-', c='blue')
g4 = f1.errorbar(	x=t4,	y=V4,		fmt='-', c='black')
g3 = f1.errorbar(	x=t3,	y=V3/10,	fmt='-', c='green')
g2 = f1.errorbar(	x=t2,	y=V2,		fmt='-', c='red')

#f1.text(0, -1.67, r'Frequenza [$Hz$]', rotation='horizontal', ha='center', va='center', fontsize=15)
#f1.text(-11.2, 0, r'Gain [$dB$]', rotation='vertical',	ha='center', va='center', fontsize=15)

f1.grid(True)
#f1.set_ylim((-400, 1000))
f1.set_xlim((-1.15,1.15))

f1.text(-1.29, 0.1, u'd.d.p. [$V$]', size=14, va='center', ha='center',rotation='90')
f1.set_xlabel(u'Tempo [$ms$]', labelpad=0, fontsize=14)

f1.legend((g2, g3, g4), ('sonda sottocompensata', 'sonda compensata', 'sonda sovracompensata' ), 'lower center', prop={'size': 13})
    
######

# questo imposta i bordi del grafico
fig1.subplots_adjust(left=0.08, right=0.98, top=0.93, bottom=0.09, hspace=0.085, wspace=0.05)
# mostra grafico
plt.show()
