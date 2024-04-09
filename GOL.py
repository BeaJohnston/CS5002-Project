import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to initialize the grid with random initial state
def initialize_grid(rows, cols):
    return np.random.choice([0, 1], size=(rows, cols))

# Function to update the grid for each generation using recursion
def update_grid(grid):
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
    def count_neighbors_recursive(grid, current_i, current_j, rows, cols, offsets):
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
    while b != 0:
        a, b = b, a % b
    return a

# Function to simulate Conway's Game of Life using recursion and the Euclidean algorithm
def simulate_game(rows, cols, frames):
    grid = initialize_grid(rows, cols)
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')

    def animate(frameNum):
        nonlocal grid
        grid = update_grid(grid)
        img.set_array(grid)
        return img,

    ani = FuncAnimation(fig, animate, frames=frames, interval=100, blit=True)
    plt.show()

def main():
    # Initialize grid size
    rows, cols = 50, 50

    # Simulate Conway's Game of Life
    simulate_game(rows, cols, frames=100)

if __name__ == "__main__":
    main()