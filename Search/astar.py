import math
import heapq

class cell:
    def __init__(self):
        self.parent_i = 0 # parent cell's row index
        self.parent_j = 0 # parent cell's col index
        self.f = float('inf') # total cost of the cell = h(n) + g(n)
        self.g = float('inf') # cost from start to this cell
        self.h = 0 # Heuristic cost from this cell to destination


# Size of the grid
ROW: int = 9
COL: int = 10

# Check if the cell is valid within the grid:
def isValid(r,c):
    return 0<=r<ROW and 0<=c<COL

# Check if the cell is unblocked
def is_unblocked(grid, row, col):
    return grid[row][col] == 1

# Check if the cell is the destination:
def is_destination(row, col, dest):
    return row == dest[0] and col == dest[1]

# calculate the heuristic fn of a cell (euclidean or manhattan distance)
def heuristic_fn(row, col, dest):
    return ((row - dest[0])**2 + (col - dest[1])**2) ** 0.5

# trace the path from source to destination:
def trace_path(cell_details, dest):
    print("THE PATH: ")
    path = []
    row = dest[0]
    col = dest[1]

    # trace the path from the parent to the destination using the parent's cell
    while not (cell_details[row][col].parent_i == row and cell_details[row][col].parent_j == col):
        path.append((row, col))
        temp_row = cell_details[row][col].parent_i
        temp_col = cell_details[row][col].parent_j
        row = temp_row
        col = temp_col

    # add the source to the path:
    path.append((row, col))

    path.reverse()

    for i in path:
        print(f"-> {i} ")
    print()

# implement the a-star search algorithm
def a_star_search(grid, dest, src):
    # check if the source and destination are valid
    if not isValid(dest[0], dest[1]) or not isValid(src[0], src[1]):
        print("Source or destination is invalid")
        return

    # check if the source and destination are unblocked:
    if not is_unblocked(grid, dest[0], dest[1]) or not is_unblocked(grid, src[0], src[1]):
        print("Source or the destination is blocked")
        return

    # Initialise the visited cells:
    closed_list = [[False for _ in range(COL)] for i in range(ROW)]
    # Initialise the details of each cell:
    cell_details = [[Cell() for _ in range(COL)] for i in range(ROW)]

    # Initialise the start cell details:
    i = src[0]
    j = src[1]
    cell_details[i][j].f = 0
    cell_details[i][j].g = 0
    cell_details[i][j].h = 0
    cell_details[i][j].parent_i = i
    cell_details[i][j].parent_j = j

    # Initialise the open list, cells to be visited with the start cell:
    open_list = []
    heapq.heappush(open_list, (0, 0, i, j))

    # Initialise the flag for whether the destination is found:
    found_dest: bool = False

    # Main algorithm:
    while len(open_list) > 0:
        # Pop the cell with the smallest f value from the open list:
        p = heapq.heappop(open_list)
        #Mark the cells as visited:
        i = p[1]
        j = p[2]
        closed_list[i][j] = True

        # For each direction check the successors
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dir in directions:
            new_i = i + dir[0]
            new_j = j + dir[1]

            # If the successor is valid, unblocked and not visited:
            if isValid(new_i, new_j) and is_unblocked(grid, new_i, new_j) and not closed_list[new_i][new_j]:
                # If the successor is the destination:
                if is_destination(new_i, new_j, dest):
                    # Set the parent of the destination cell:
                    cell_details[new_i][new_j].parent_i = i
                    cell_details[new_i][new_j].parent_j = j
                    print("The destination cell is found")
                    # trace and print the path from source to destination:
                    trace_path(cell_details, dest)
                    found_dest = True
                    return
                else:
                    # Calculate new f, g, h values:
                    g_new = cell_details[i][j].g + 1.0
                    h_new = heuristic_fn(new_i, new_j, dest)
                    f_new = g_new + h_new

                    # If the cell is not in the open list or the new f value is smaller:
                    if cell_details[new_i][new_j].f  == float('inf') or cell_details[new_i][new_j].f > f_new:
                        # Add the cell to the open_list
                        heapq.heappush(open_list, (f_new, new_i, new_j))
                        # Update the cell details:
                        cell_details[new_i][new_j].f = f_new
                        cell_details[new_i][new_j].g = g_new
                        cell_details[new_i][new_j].h = h_new
                        cell_details[new_i][new_j].parent_i = i
                        cell_details[new_i][new_j].parent_j = j

    # if the destination is not found after visiting all cells:
    if not found_dest:
        print("Failed to find the destination")



def main():
    # Define the grid (1 for unblocked, 0 for blocked)
    grid = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]
    ]

    # Define the source and destination
    src = [8, 0]
    dest = [0, 0]

    # Run the A* search algorithm
    a_star_search(grid, src, dest)

if __name__ == "__main__":
    main()
