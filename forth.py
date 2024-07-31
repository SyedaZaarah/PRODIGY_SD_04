def print_grid(grid):
    """Print the Sudoku grid."""
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))


def find_empty_location(grid):
    """Find an empty location in the grid. Returns (row, col) or None if no empty locations."""
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None


def is_valid(grid, row, col, num):
    """Check if it's valid to place num in grid[row][col]."""
    # Check if num is not in the current row
    if num in grid[row]:
        return False

    # Check if num is not in the current column
    if num in [grid[i][col] for i in range(9)]:
        return False

    # Check if num is not in the 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True


def solve_sudoku(grid):
    """Solve the Sudoku puzzle using backtracking."""
    empty_location = find_empty_location(grid)

    if not empty_location:
        return True  # Puzzle solved

    row, col = empty_location

    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            # If not solvable, reset the cell
            grid[row][col] = 0

    return False


# Example usage:
if __name__ == "__main__":
    # Define an unsolved Sudoku grid (0 represents an empty cell)
    sudoku_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    if solve_sudoku(sudoku_grid):
        print("Sudoku solved successfully!")
        print_grid(sudoku_grid)
    else:
        print("No solution exists for the Sudoku puzzle.")
