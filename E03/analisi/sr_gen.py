from math import *			# da math importo tutto # non devo utilizzare il namespace (es: np per numpy)

from matplotlib import *		# da matplotlib importo tutto # non devo utilizzare il namespace (es: np per numpy)
import matplotlib.pyplot as plt
import numpy as np			# importo numpy come np

from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA

#### dati ####
data01 = np.genfromtxt("../dati/scope_9.csv", delimiter=',')
t_01 = data01[2:,0]
VS_01 = data01[2:,1]
#data02 = np.genfromtxt("../dati/scope_1.csv", delimiter=',')
#t_02 = data02[2:,0]
#VS_02 = data02[2:,1]

rcParams['font.size'] = 15
# Creo un grafico la dimensione è in pollici
fig1 = plt.figure(figsize=(15, 7), dpi=65)
# Titolo del grafico
fig1.suptitle("Circuito sommatore: onda sinusoidale e onda quadra", y=0.97, fontsize=17)

# GRAFICO
f1 = host_subplot(111, axes_class=AA.Axes)

out1 = f1.errorbar(x=t_01*1E9, y=VS_01, fmt='-', c='black', linewidth=2)
p10h = f1.axhline(y=-8, xmin=0, xmax=1, c='gray', ls='-.', lw=1.5)
p10v = f1.axvline(x=-9, ymin=0, ymax=1, c='gray', ls='-.', lw=1.5)
p90h = f1.axhline(y=8, xmin=0, xmax=1, c='gray', ls='-.', lw=1.5)
p90v = f1.axvline(x=16, ymin=0, ymax=1, c='gray', ls='-.', lw=1.5)

points = f1.plot([-9, 16], [-8, 8], c='red', marker='o', ls='')

p10t = f1.text(-9-2, -8+0.2, r'$P_{10\%}$', rotation='horizontal',
	ha='right', va='bottom', fontsize=22)
p90t = f1.text(16+2, 8-0.2, r'$P_{90\%}$', rotation='horizontal',
	ha='left', va='top', fontsize=22)

f1.text(380/2-90, -16.7, r'tempo [$ns$]', rotation='horizontal',
	ha='center', va='center', fontsize=15)
f1.text(-11.2E3, 0, r'd.d.p. [$V$]', rotation='vertical',
	ha='center', va='center', fontsize=15)

f1.set_xlim((-0.09E3,0.29E3))
#f1.set_ylim((-1.6,1.6))

f1.grid(True)

# plotta la legenda
#f1.legend([out1, in1, in2], ['Output sommatore', 'Generatore 1', 'Generatore 2'])

# questo imposta i bordi del grafico
fig1.subplots_adjust(left=0.05, right=0.98,
    top=0.92, bottom=0.08, hspace=0.18, wspace=0.03)

# mostra grafico
plt.show()
