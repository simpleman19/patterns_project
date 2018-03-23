import matplotlib.pyplot as plt
from walker import Walker

w = Walker()
w.fill_walk()

plt.scatter(w.x_values, w.y_values, s=15)
plt.show()
