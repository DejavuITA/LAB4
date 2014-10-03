from math import *			# da math importo tutto # non devo utilizzare il namespace (es: np per numpy)

from matplotlib import *		# da matplotlib importo tutto # non devo utilizzare il namespace (es: np per numpy)
import matplotlib.pyplot as plt
import numpy as np			# importo numpy come np

from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA

#### dati ####
data01 = np.genfromtxt("../dati/nuovi/tt_0210_05.csv", delimiter=',')
t_01 = data01[2:,0]
VS_01 = data01[2:,1]
VS_02 = data01[2:,2]

rcParams['font.size'] = 15
# Creo un grafico la dimensione è in pollici
fig1 = plt.figure(figsize=(15, 7), dpi=65)
# Titolo del grafico
fig1.suptitle("Massima corrente pilotabile dall'opamp", y=0.97, fontsize=17)

# GRAFICO
f1 = host_subplot(111, axes_class=AA.Axes)

l_zero = f1.axhline(y=0, xmin=0, xmax=1, c='0.5', ls='-', lw=2)

out1 = f1.errorbar(x=t_01*1E3, y=VS_01, fmt='-', c='black', linewidth=2)
out2 = f1.errorbar(x=t_01*1E3, y=VS_02, fmt='-', c='green', linewidth=2)

l_max = f1.axhline(y=1.96, xmin=0, xmax=1, c='gray', ls='--', lw=1.5)
l_min = f1.axhline(y=-3.36, xmin=0, xmax=1, c='gray', ls='--', lw=1.5)

f1.text(-0.5, 2.05, r'$V = 1.96V$', rotation='horizontal',
	ha='center', va='bottom', fontsize=18)
f1.text(-1.5, -3.36+0.5, r'$V = -3.36V$', rotation='horizontal',
	ha='center', va='center', fontsize=18)

f1.text(0, -7.75, r'tempo [$ms$]', rotation='horizontal',
	ha='center', va='center', fontsize=15)
f1.text(-2.85, 0, r'd.d.p. [$V$]', rotation='vertical',
	ha='center', va='center', fontsize=15)

f1.set_xlim((-2.7,2.7))
f1.set_ylim((-7,7))
#f1.yaxis.set_ticks((-6,-4,-3.36,-2,0,1.96,2,4,6))

f1.grid(True)

# plotta la legenda
#f1.legend([out1, in1, in2], ['Output sommatore', 'Generatore 1', 'Generatore 2'])

# questo imposta i bordi del grafico
fig1.subplots_adjust(left=0.045, right=0.98,
    top=0.92, bottom=0.08, hspace=0.18, wspace=0.03)

# mostra grafico
plt.show()
