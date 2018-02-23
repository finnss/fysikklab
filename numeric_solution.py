from math import sin, cos

from iptrack import iptrack
from trvalues import trvalues

import numpy as np
import matplotlib.pyplot as plt

mass = 2.7  # m (gram)
radius = 0.02  # r (meter)

inertia = (2/3) * mass * radius  # I
air_resistance = 0.001436236  # L

c = inertia/(mass * radius ** 2)
g = 9.81

data_number = 12
polynomial = iptrack('data/' + str(data_number) + '.txt')  # 15 degree polynomial

number_of_data_points = int((len(open('data/' + str(data_number) + '.txt').read().split(' ')) - 4) / 3)
print('number_of_data_points,', number_of_data_points)


def get_acceleration(position):
    current_tr = trvalues(x=position, p=polynomial)  # [y, dydx, d2ydx2, alpha, R]
    print('current tr (y, dydx, d2ydx2, alpha, R)', current_tr)
    angle = current_tr[3]
    R = current_tr[4]

    return (g/(1 + c)) \
        * (sin(angle) - (radius/R) * cos(angle)) \
        + (air_resistance / (mass * (1 + c)))


def eulers_method(m, D, n=number_of_data_points, h=0.01,):
    # initial values
    t_0 = 0.0
    x_0 = 0.21  # meter
    v_0 = 0.0

    t = np.zeros(n + 1)
    x = np.zeros(n + 1)
    v = np.zeros(n + 1)
    t[0] = t_0
    x[0] = x_0
    v[0] = v_0

    for i in range(n):
        # Euler's method
        a = get_acceleration(x[i])
        v_new = v[i] + h * a
        x_new = x[i] + h * v[i]
        print('iteration', str(i), '- acceleration', a, '\t velocity', v_new, '\tposition', x_new)

        v[i + 1] = v_new
        x[i + 1] = x_new
        t[i + 1] = t[i] + h

    return x, v, t


x, v, t = eulers_method(mass, air_resistance)
print('position iterations: ', x)
print('velocity iterations: ', v)
print('time iterations: ', t)



plt.figure()
plt.plot(t, x)  # plotting the position vs. time: x(t)
plt.xlabel(r'$t$')
plt.ylabel(r'$x(t)$')
plt.grid()
plt.savefig('plots/' + str(data_number) + '_x.png', bbox_inches='tight')
print('Position plot saved')

plt.figure()
plt.plot(t, x)  # plotting the position vs. time: x(t)
plt.xlabel(r'$t$')
plt.ylabel(r'$x(t)$')
plt.grid()
plt.savefig('plots/' + str(data_number) + '_x.png', bbox_inches='tight')
print('Position plot saved')

plt.figure()
plt.plot(t, v)  # plotting the velocity vs. time: v(t)
plt.xlabel(r'$t$')
plt.ylabel(r'$v(t)$')
plt.grid()
plt.savefig('plots/' + str(data_number) + '_v.png', bbox_inches='tight')
plt.close()
print('Velocity plot saved')
