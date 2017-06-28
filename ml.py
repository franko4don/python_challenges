import matplotlib.pyplot as plt
from random import randint

x = [randint(0, x) for x in range(200)]
y = [randint(0, x) for x in range(0, 400, 2)]
x1 = [randint(0, x) for x in range(0, 800, 4)]
y1 = [randint(0, x) for x in range(0, 1600, 8)]

print(x)
plt.scatter(y1, y, x1, x)
plt.grid(True, color='g')
plt.show()


