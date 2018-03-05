from math import sin, cos, sqrt, log, exp

from iptrack import iptrack
from trvalues import trvalues

import numpy as np
import matplotlib.pyplot as plt
import re

mass = 2.7  # m (gram)
radius = 0.02  # r (meter)

inertia = (2/3) * mass * radius  # I
air_resistance = 0.001436236  # L

c = inertia/(mass * radius ** 2)
g = 981
h = 0.01

data_number = 12
data = open('data/' + str(data_number) + '.txt').read()

t = []
x = []
y = []
v = []
e = []

c = (2/3)

data_list = re.split(' |\n', data)

for i, data_point in enumerate(data_list[4:-1]):
    print('data point', i, data_point)
    if i % 3 is 0:  # time
        t.append(float(data_point))
    elif i % 3 is 1:  # x
        x.append(float(data_point))
    elif i % 3 is 2:  # y
        y.append(float(data_point))
        # End of row, so we calculate v for this row
        dx = x[len(x) - 1] - x[len(x) - 2]
        dy = y[len(y) - 1] - y[len(y) - 2]
        dt = t[len(t) - 1] - t[len(t) - 2]
        if dt == 0 or dt == 0.0:
            dt = h
        v_x = dx / dt
        v_y = dy / dt
        velocity = sqrt(v_x ** 2 + v_y ** 2)
        v.append(velocity)

        kinetic = (1/2) * mass * (velocity ** 2)
        potential = mass * g * y[len(y) - 1]

        rotation = (c / 2) * mass * (velocity ** 2)

        total_energy = kinetic + potential + rotation
        print('kinetic', kinetic, 'potential', potential, 'total', total_energy)
        e.append(total_energy)
print('e', e)

plt.figure()
plt.plot(t, e)  # plotting the velocity vs. time: v(t)
plt.xlabel(r'$t$')
plt.ylabel(r'$e(t)$')
plt.grid()
plt.savefig('plots/' + str(data_number) + '_e.png', bbox_inches='tight')
plt.close()
print('Energy plot saved')

print('log e', len(np.log(e)), np.log(e))
print('t', len(t), t)

# Uten log-space:
fit = np.polyfit(np.array(t), e, 6)
a = np.polyval(fit, t)

"""
# Med log-space (funker ikke)
fit = np.polyfit(np.array(t), np.log(e), 1)
a = np.exp(fit[1]) * np.exp(fit[0] * np.array(t))

print('fit', fit)
a = np.array(np.exp(fit[1]) * np.exp(np.array(t) * float(fit[0])))
# a = np.array(fit[1] + fit[0]*np.array(t))

print('a', a)
"""
plt.figure()
plt.plot(t, a)  # plotting the velocity vs. time: v(t)
plt.xlabel(r'$t$')
plt.ylabel(r'$e(t)$')
plt.grid()
plt.savefig('plots/' + str(data_number) + '_fit.png', bbox_inches='tight')
plt.close()
print('Energy loss plot saved')
