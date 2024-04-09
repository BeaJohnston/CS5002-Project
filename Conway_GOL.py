import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to initialize the grid with random initial state
def initialize_grid(rows, cols):
    return np.random.choice([0, 1], size=(rows, cols))

# Function to update the grid for each generation
def update_grid(frameNum, img, grid):
    newGrid = grid.copy()
    for i in range(rows):
        for j in range(cols):
            # Compute the sum of the neighbors' values
            total = int((grid[i, (j-1)%cols] + grid[i, (j+1)%cols] +
                         grid[(i-1)%rows, j] + grid[(i+1)%rows, j] +
                         grid[(i-1)%rows, (j-1)%cols] + grid[(i-1)%rows, (j+1)%cols] +
                         grid[(i+1)%rows, (j-1)%cols] + grid[(i+1)%rows, (j+1)%cols]))
            # Apply the rules of the game
            # make the parameter of a function
            if grid[i, j] == 1:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = 0
            else:
                if total == 3:
                    newGrid[i, j] = 1
    img.set_array(newGrid)
    grid[:] = newGrid[:]
    return img,

def main():
    # Initialize grid size
    global rows, cols
    rows, cols = 50, 50

    # Create initial random grid
    grid = initialize_grid(rows, cols)

    # Create the animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = FuncAnimation(fig, update_grid, fargs=(img, grid), frames=100, interval=100, blit=True)

    plt.show()

if __name__ == "__main__":
    main()
