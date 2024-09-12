import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


class MazeVisualizer:
    def __init__(self):
        # Define a discrete colormap
        self._colors = ['black', 'white', 'green', 'red', 'blue', 'grey', 'yellow', 'pink']
        self._cmap = mcolors.ListedColormap(self._colors)
        self._bounds = [0, 1.5, 2.5, 3.5, 4.5, 5.5, 6.6, 7.5, 8.5]  # Define boundaries for each color
        self._norm = mcolors.BoundaryNorm(self._bounds, self._cmap.N)
        
    def play(self, mazes, interval=1.5):
        for maze in mazes:
            plt.imshow(maze, cmap=self._cmap, norm=self._norm, interpolation='nearest')
            plt.pause(interval) # seconds
            
    def display_single_state(self, maze, interval=1.0):
        plt.imshow(maze, cmap=self._cmap, norm=self._norm, interpolation='nearest')
        plt.pause(interval) # seconds
        


if __name__ == "__main__":
    # Simulating we have mazes generated by the maze solver
    example_maze = np.mat([[3, 2, 2, 1],
                        [1, 2, 1, 1],
                        [2, 2, 2, 2],
                        [4, 1, 2, 2]])
    end_maze = np.mat([[3, 7, 2, 1],
                    [1, 7, 1, 1],
                    [7, 7, 2, 2],
                    [4, 1, 2, 2]])
    mazes_to_play = [example_maze, end_maze]
    
    # visualizing the mazes
    vis = MazeVisualizer()
    vis.play(mazes_to_play, interval=2.0)