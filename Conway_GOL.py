import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
###################################################################################################################################################################
#This function initializes a grid with random initial states.
#Parameters:
#rows: The number of rows in the grid.
#cols: The number of columns in the grid.
#Returns:
#A NumPy array representing the initialized grid with random 0s and 1s.
###################################################################################################################################################################
    
def initialize_grid(rows, cols):
    return np.random.choice([0, 1], size=(rows, cols))

###################################################################################################################################################################
#This function updates the grid for each generation based on the rules of Conway's Game of Life.
#Parameters:
#frameNum: The current frame number of the animation (unused in the function).
#img: The image object representing the grid plot.
#grid: The NumPy array representing the current state of the grid.
#Returns:
#The updated image object -> img
#It computes the next state of the grid based on the rules of Conway's Game of Life, which includes counting the neighbors of each cell and applying the rules to determine whether a cell lives, dies, or becomes alive.
#The updated grid is then assigned to the image object img, and the function returns it.
###################################################################################################################################################################
 

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
