from math import *			# da math importo tutto # non devo utilizzare il namespace (es: np per numpy)

from matplotlib import *		# da matplotlib importo tutto # non devo utilizzare il namespace (es: np per numpy)
import matplotlib.pyplot as plt
import numpy as np			# importo numpy come np

from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA

#### dati ####
data01 = np.genfromtxt("../dati/scope_10.csv", delimiter=',') ##### ← cambiare qui con i file giusti
t_01 = data01[2:,0]
VS_01 = data01[2:,1]
VS_02 = data01[2:,2]

data02 = np.genfromtxt("../dati/scope_10.csv", delimiter=',') ##### ← cambiare qui con i file giusti
t_02 = data02[2:,0]
VS_11 = data02[2:,1]
VS_12 = data02[2:,2]

rcParams['font.size'] = 15
# Creo un grafico la dimensione è in pollici
fig1 = plt.figure(figsize=(17, 6), dpi=65)
# Titolo del grafico
fig1.suptitle("Slew Rate: salita e discesa", y=0.97, fontsize=17)

# GRAFICO 1
f1 = host_subplot(121, axes_class=AA.Axes)

out1 = f1.errorbar(x=t_01*1E6, y=VS_01, fmt='-', c='0.1', linewidth=1)
out2 = f1.errorbar(x=t_01*1E6, y=VS_02, fmt='-', c='red', linewidth=1)

points = f1.plot([0.00048E3, 0.00208E3, 0.0163E3], [-8, -5, 8], c='black', marker='o', ls='')

p10h = f1.axhline(y=-8, xmin=0, xmax=1, c='gray', ls='-.', lw=1.5)
p25h = f1.axhline(y=-5, xmin=0, xmax=1, c='gray', ls='-.', lw=1.5)
p90h = f1.axhline(y=8, xmin=0, xmax=1, c='gray', ls='-.', lw=1.5)
p10v = f1.axvline(x=0.00048E3, ymin=0, ymax=1, c='gray', ls='-.', lw=1.5)
p25v = f1.axvline(x=0.00208E3, ymin=0, ymax=1, c='gray', ls='-.', lw=1.5)
p90v = f1.axvline(x=0.0163E3, ymin=0, ymax=1, c='gray', ls='-.', lw=1.5)

p10t = f1.text((0.00048+0.0002)*1E3, -8-0.2, r'$P_{10\%}$', rotation='horizontal',
	ha='left', va='top', fontsize=22)
p25t = f1.text((0.00208+0.0002)*1E3, -5-0.2, r'$P_{25\%}$', rotation='horizontal',
	ha='left', va='top', fontsize=22)
p90t = f1.text((0.0163+0.0002)*1E3, 8-0.2, r'$P_{90\%}$', rotation='horizontal',
	ha='left', va='top', fontsize=22)

f1.text(0.022E3/2-0.002E3, -17.3, r'tempo [$\mu s$]', rotation='horizontal',
	ha='center', va='center', fontsize=15)
f1.text(-3, 0, r'd.d.p. [$V$]', rotation='vertical',
	ha='center', va='center', fontsize=15)

f1.set_xlim((-0.002E3,0.02E3))
#f1.set_ylim((-1.6,1.6))

f1.grid(True)

# GRAFICO 2
f2 = host_subplot(122, axes_class=AA.Axes)

A=-0.002E3
B=0.02E3

out1 = f2.errorbar(x=t_02*1E6, y=VS_11, fmt='-', c='0.1', linewidth=1)
out2 = f2.errorbar(x=t_02*1E6, y=VS_12, fmt='-', c='red', linewidth=1)

points = f2.plot([0.00048E3, 0.00208E3, 0.0163E3], [-8, -5, 8], c='black', marker='o', ls='')

p10h = f2.axhline(y=-8, xmin=0, xmax=1, c='gray', ls='-.', lw=1.5)
p90h = f2.axhline(y=8, xmin=0, xmax=1, c='gray', ls='-.', lw=1.5)
p10v = f2.axvline(x=0.00048E3, ymin=0, ymax=1, c='gray', ls='-.', lw=1.5)
p90v = f2.axvline(x=0.0163E3, ymin=0, ymax=1, c='gray', ls='-.', lw=1.5)

p10t = f2.text((0.00048+0.0002)*1E3, -8-0.2, r'$P_{10\%}$', rotation='horizontal',
	ha='left', va='top', fontsize=22)
p90t = f2.text((0.0163+0.0002)*1E3, 8-0.2, r'$P_{90\%}$', rotation='horizontal',
	ha='left', va='top', fontsize=22)

f2.text((B-A)/2+A, -17.3, r'tempo [$\mu s$]', rotation='horizontal',
	ha='center', va='center', fontsize=15)
f2.text(21, 0, r'd.d.p. [$V$]', rotation='vertical',
	ha='center', va='center', fontsize=15)

f2.set_xlim((A,B))
#f2.set_ylim((-1.6,1.6))
f3 = f2.twin()
#f3.set_yticks((-5,-4,-2,0,2,4,5))
f3.axis["top"].major_ticklabels.set_visible(False)
f2.axis["left"].major_ticklabels.set_visible(False)

f2.grid(True)

# plotta la legenda
#f1.legend([out1, in1, in2], ['Output sommatore', 'Generatore 1', 'Generatore 2'])

# questo imposta i bordi del grafico
fig1.subplots_adjust(left=0.04, right=0.96,
    top=0.925, bottom=0.10, hspace=0.18, wspace=0.03)

# mostra grafico
plt.show()
