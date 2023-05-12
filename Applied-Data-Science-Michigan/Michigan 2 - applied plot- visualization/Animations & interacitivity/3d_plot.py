import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [5, 6, 7, 8, 2, 5, 6, 3, 7, 2]
z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


fig, axes = plt.subplots(nrows=2, ncols=2, subplot_kw={'projection': '3d'}, figsize=(10,10))

colors = ['r', 'g', 'b', 'y']

for c , ax in zip(colors, axes.flat):
    ax.scatter(x, y, z)
    ax.set(xlabel='x', ylabel='y', zlabel='z', facecolor=c)
    
fig.set(facecolor='lightgray')
plt.show()