import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

example_maze = np.mat([[3, 2, 2, 1],
                       [1, 2, 1, 1],
                       [2, 2, 2, 2],
                       [4, 1, 2, 2]])

end_maze = np.mat([[3, 7, 2, 1],
                   [1, 7, 1, 1],
                   [7, 7, 2, 2],
                   [4, 1, 2, 2]])

maze_to_play = [example_maze, end_maze]

cmap = mcolors.LinearSegmentedColormap.from_list(
    'custom_cmap',
    [(1, 'black'),
     (2, 'white'),
     (3, 'green'),
     (4, 'red'),
     (5, 'blue'),
     (6, 'grey'),
     (7, 'yellow'),
     (8, 'purple'),
     ]
)

# Define a discrete colormap
colors = ['black', 'white', 'green', 'red', 'blue', 'grey', 'yellow', 'purple']
cmap = mcolors.ListedColormap(colors)
bounds = [0, 1.5, 2.5, 3.5, 4.5, 5.5, 6.6, 7.5, 8.5]  # Define boundaries for each color
norm = mcolors.BoundaryNorm(bounds, cmap.N)

for maze in maze_to_play:
    plt.imshow(maze, cmap=cmap, norm=norm, interpolation='nearest')
    plt.pause(1.0)