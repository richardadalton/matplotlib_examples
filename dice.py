import matplotlib.pyplot as plt
from random import randint


def throw_dice(n):
    return sum([randint(1, 6) for dice in range(n)])

throws = [ throw_dice(10) for t in range(100000)]

print(throws)

plt.hist(throws)
plt.show()