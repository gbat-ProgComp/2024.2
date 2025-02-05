import matplotlib.pyplot as plt
import math

# URL: https://matplotlib.org

MAX = 720
graus = [g for g in range (MAX)]

plt.plot(graus, [math.sin(g/180*3.14) for g in graus], 'r')
plt.plot(graus, [math.cos(g/180*3.14) for g in graus], 'g')
plt.ylabel('sin(x) e cos(x)')
plt.show()
