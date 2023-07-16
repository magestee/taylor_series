""" math module: """
# import math

# x = 2
# n = 20
# taylor_term = 0

# for i in range(n):
#     taylor_term += x**i/math.factorial(i)

# print(taylor_term)
# print(math.exp(2))

""" numpy """
import numpy as np
import matplotlib.pyplot as plt
from math import factorial


x = np.linspace(-10, 10, 1000)
y = np.zeros(len(x))
n = 15

figure = plt.figure()

for i in range(n):
    taylor_term = (-1)**i * x**(2*i)/factorial(2*i)
    y = np.add(y, taylor_term)

    figure.clear()

    ax = figure.subplots()
    ax.plot(x,y)
    ax.set_xlabel('x')
    ax.set_ylabel('cos(x)')

    """ f-string """
    # ax.set_title(f"Terms: {i+1}")

    ax.set_title("Tems: {}".format(i+1))

    plt.xlim(min(x), max(x))
    plt.ylim(-2,2)

    plt.grid()
    plt.draw()

    plt.pause(0.1)

plt.show()