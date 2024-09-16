import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

class MazeVisualizer:
    def __init__(self):
        # Define a discrete colormap
        self._colors = ['purple', 'black', 'white', 'blue', 'red', 'orange', 'purple', 'yellow']
        self._cmap = mcolors.ListedColormap(self._colors)
        self._bounds = [-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.6, 7.5]  # Define boundaries for each color
        self._norm = mcolors.BoundaryNorm(self._bounds, self._cmap.N)
        
        # Set matplotlib to full screen by default
        manager = plt.get_current_fig_manager()
        manager.full_screen_toggle()

            
    def display_single_state(self, maze, interval=1.0):
        plt.clf()
        plt.imshow(maze, cmap=self._cmap, norm=self._norm, interpolation='nearest')
        plt.pause(interval) # seconds
        