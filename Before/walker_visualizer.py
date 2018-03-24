import matplotlib.pyplot as plt
from walker import Walker

while True:
    w = Walker(50000)
    w.fill_walk()
    
    plt.figure(figsize=(10, 6))
    
    point_numbers = list(range(w.num_points))
    plt.scatter(w.x_values, w.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
    
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(w.x_values[-1], w.y_values[-1], c='red', edgecolors='none', s=100)

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)    
 
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
