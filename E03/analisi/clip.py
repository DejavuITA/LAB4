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
fig1.suptitle("Co", y=0.97, fontsize=17)

# GRAFICO
f1 = host_subplot(111, axes_class=AA.Axes)

out1 = f1.errorbar(x=t_01*1E6, y=VS_01, fmt='-', c='black', linewidth=2)
out2 = f1.errorbar(x=t_01*1E6, y=VS_02+1.7, fmt='-', c='green', linewidth=2)

p10h = f1.axhline(y=-8, xmin=0, xmax=1, c='gray', ls='-.', lw=1.5)
p90h = f1.axhline(y=8, xmin=0, xmax=1, c='gray', ls='-.', lw=1.5)
p10v = f1.axvline(x=0.0589E3, ymin=0, ymax=1, c='gray', ls='-.', lw=1.5)
p90v = f1.axvline(x=0.03555E3, ymin=0, ymax=1, c='gray', ls='-.', lw=1.5)

points = f1.plot([0.0589E3, 0.03555E3], [-8, 8], c='black', marker='o', ls='')

p10t = f1.text(0.0589E3+0.0002E3, -8+0.2, r'$P_{10\%}$', rotation='horizontal',
	ha='left', va='bottom', fontsize=22)
p90t = f1.text(0.03555E3+0.0004E3, 8+0.2, r'$P_{90\%}$', rotation='horizontal',
	ha='left', va='bottom', fontsize=22)

f1.text(0.11E3/2-0.01E3, -16.8, r'tempo [$\mu s$]', rotation='horizontal',
	ha='center', va='center', fontsize=15)
f1.text(-0.0125E3, 0, r'd.d.p. [$V$]', rotation='vertical',
	ha='center', va='center', fontsize=15)

#f1.set_xlim((-0.01E3,0.1E3))
#f1.set_ylim((-1.6,1.6))

f1.grid(True)

# plotta la legenda
#f1.legend([out1, in1, in2], ['Output sommatore', 'Generatore 1', 'Generatore 2'])

# questo imposta i bordi del grafico
fig1.subplots_adjust(left=0.045, right=0.98,
    top=0.92, bottom=0.08, hspace=0.18, wspace=0.03)

# mostra grafico
plt.show()
