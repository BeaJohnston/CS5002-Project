import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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
    if i < 0 or j < 0 or i >= rows or j >= cols:
        return 0
    if grid[i, j] == 1:
        return 1
    return (count_neighbors(grid, i-1, j, rows, cols) +
            count_neighbors(grid, i+1, j, rows, cols) +
            count_neighbors(grid, i, j-1, rows, cols) +
            count_neighbors(grid, i, j+1, rows, cols) +
            count_neighbors(grid, i-1, j-1, rows, cols) +
            count_neighbors(grid, i-1, j+1, rows, cols) +
            count_neighbors(grid, i+1, j-1, rows, cols) +
            count_neighbors(grid, i+1, j+1, rows, cols))

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

    ani = animation.FuncAnimation(fig, animate, frames=frames, interval=100, blit=True)
    plt.show()

# Initialize grid size
rows, cols = 50, 50

# Simulate Conway's Game of Life
simulate_game(rows, cols, frames=100)
