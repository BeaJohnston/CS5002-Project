import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to initialize the grid with random initial state
def initialize_grid(rows, cols):
    '''
    This function initializes a grid with random initial states.
    Parameters:
    rows: The number of rows in the grid.
    cols: The number of columns in the grid.
    Returns:
    A NumPy array representing the initialized grid with random 0s and 1s.
    Description:
    It utilizes NumPy's random.choice() function to randomly select 0 or 1 for each cell in the grid based on a given probability distribution.
    The size of the grid is determined by the rows and cols parameters.
    The function returns the initialized grid as a NumPy array.
    '''
    return np.random.choice([0, 1], size=(rows, cols))

# Function to update the grid for each generation using recursion
def update_grid(grid):
    '''
    This function updates the grid for each generation based on the rules of Conway's Game of Life using recursion.
    Parameters:
    grid: The current state of the grid represented as a NumPy array.
    Returns:
    A new NumPy array representing the updated grid after applying the rules of the game.
    Description:
    It iterates over each cell in the grid, computes the total count of live neighboring cells for each cell using the count_neighbors() function.
    Based on the count of live neighbors and the current state of the cell, it updates the cell's state according to the rules of Conway's Game of Life.
    The updated grid is returned as a new NumPy array.
    '''
    rows, cols = grid.shape
    new_grid = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            total = count_neighbors(grid, i, j, rows, cols)
            # Apply the rules of the game
            if grid[i, j] == 1:
                if (total < 2) or (total > 3):
                    new_grid[i, j] = 0
                else:
                    new_grid[i, j] = 1
            else:
                if total == 3:
                    new_grid[i, j] = 1
    return new_grid

# Function to count live neighboring cells using recursion
def count_neighbors(grid, i, j, rows, cols):
    '''
    This function recursively counts the live neighboring cells of a specified cell (i, j) in the grid.
    Parameters:
    grid: The current state of the grid represented as a NumPy array.
    i: The row index of the cell for which neighbors are to be counted.
    j: The column index of the cell for which neighbors are to be counted.
    rows: The total number of rows in the grid.
    cols: The total number of columns in the grid.
    Returns:
    The count of live neighboring cells for the specified cell (i, j).
    Description:
    It utilizes a nested recursive function count_neighbors_recursive() to iterate over the neighboring cells and count the live ones.
    The neighboring cells are determined by predefined offsets.
    The count of live neighboring cells is returned recursively.
    '''
    def count_neighbors_recursive(grid, current_i, current_j, rows, cols, offsets):
        '''
        This is a helper function used by the count_neighbors() function to recursively count the live neighboring cells of a specified cell (current_i, current_j) in the grid.
        Parameters:
        grid: The current state of the grid represented as a NumPy array.
        current_i: The row index of the current cell for which neighbors are being counted.
        current_j: The column index of the current cell for which neighbors are being counted.
        rows: The total number of rows in the grid.
        cols: The total number of columns in the grid.
        offsets: A list of tuples representing the offsets for neighboring cells.
        Returns:
        The count of live neighboring cells for the specified cell (current_i, current_j).
        Description:
        This function is designed to be called recursively within the count_neighbors() function for each neighboring cell of the current cell.
        It first checks if the offsets list is empty. If so, it returns 0, indicating no live neighboring cells were found.
        Otherwise, it takes the first offset tuple from the offsets list and calculates the row and column indices of the neighboring cell based on the current cell's indices (current_i and current_j).
        If the neighboring cell is within the bounds of the grid, it adds the value of that cell to the result and recursively calls itself with the remaining offsets in the list.
        If the neighboring cell is out of bounds, it skips counting that cell and continues with the next offset in the list.
        Finally, it returns the sum of the values of all live neighboring cells counted recursively.
        '''
        if not offsets:
            return 0
        
        di, dj = offsets[0]
        ni,  nj = current_i + di, current_j + dj

        # Skip out of bounds neighbors by not counting them
        if ni < 0 or nj < 0 or ni >= rows or nj >= cols:
            return count_neighbors_recursive(grid,current_i, current_j, rows, cols, offsets[1:])
        
        # Add current neighbor cell to count
        result = grid[ni,nj] + count_neighbors_recursive(grid,current_i, current_j, rows, cols, offsets[1:])
        return result

    # Define offsets for neighboring cells
    neighbor_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    # Start recursive neighbor count for each cell with initial offset
    return count_neighbors_recursive(grid, i, j, rows, cols, neighbor_offsets)

# Function to calculate the GCD using Euclidean algorithm
def gcd(a, b):
    '''
    This function calculates the greatest common divisor (GCD) of two integers a and b using the Euclidean algorithm.
    Parameters:
    a: The first integer.
    b: The second integer.
    Returns:
    The GCD of a and b.
    Description:
    It repeatedly calculates remainders until one of the numbers becomes zero, and then returns the non-zero number (which is the GCD).
    '''
    while b != 0:
        a, b = b, a % b
    return a

# Function to simulate Conway's Game of Life using recursion and the Euclidean algorithm
def simulate_game(rows, cols, frames):
    '''
    This function simulates Conway's Game of Life using recursion and the Euclidean algorithm.
    Parameters:
    rows: The number of rows in the grid.
    cols: The number of columns in the grid.
    frames: The total number of frames for the animation.
    Description:
    It initializes the grid using initialize_grid() function, creates a Matplotlib figure and axis for visualization.
    Defines an animate() function that updates the grid for each frame of the animation by calling update_grid() and updates the image accordingly.
    Uses FuncAnimation to animate the changes in the grid for a specified number of frames.
    The animation is displayed using plt.show()
    '''
    grid = initialize_grid(rows, cols)
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')

    def animate(frameNum):
        '''
        This function is responsible for updating the grid and the corresponding image for each frame of the animation.
        Parameters:    
        frameNum: The current frame number of the animation.
        Returns:
        The updated image object.
        Description:
        The function is defined within the simulate_game() function scope to encapsulate the animation logic.
        It takes the current frame number as input but doesn't directly use it. Instead, it updates the grid variable from the outer scope.
        Inside the function, it updates the grid by calling the update_grid() function, which computes the next generation of the game grid based on the rules of Conway's Game of Life.
        After updating the grid, it sets the updated grid as the data for the image object img using set_array().
        Finally, it returns the updated image object. This is necessary for the FuncAnimation to know which parts of the plot need to be updated for each frame.
        '''
        nonlocal grid
        grid = update_grid(grid)
        img.set_array(grid)
        return img,

    ani = FuncAnimation(fig, animate, frames=frames, interval=100, blit=True)
    plt.show()

def main():
    '''
    This is the main function that initializes the grid size and calls simulate_game() to start the simulation.
    It sets the grid size and initiates the simulation of Conway's Game of Life.
    '''
    # Initialize grid size
    rows, cols = 50, 50

    # Simulate Conway's Game of Life
    simulate_game(rows, cols, frames=100)

if __name__ == "__main__":
    main()
