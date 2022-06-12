def is_solved(grid):

    flat_list = []
    for sublist in grid:
        flat_list.extend(sublist)
        print(set(flat_list))
    if set(flat_list) != 0 and len(set(flat_list)) != 1:
        return 0
    elif set(flat_list) != 0 and 0 in set(flat_list):
        return -1

    #rows
    for x in range(0, 3):
        row = set([grid[x][0], grid[x][1], grid[x][2]])
        # print(row)
        if len(row) == 1 and grid[x][0] != 0:
            if grid[x][0] == 1:
                return 1
            elif grid[x][0] == 2:
                return 2
            elif grid[x][0] == 0:
                return grid[x][0]
    # columns
    for x in range(0,   3):
        column = set([grid[0][x], grid[1][x], grid[2][x]])
        # print(f'col {column}')
        if len(column) == 1 and grid[0][x] != 0:
            if grid[0][x] == 1:
                return 1
            elif grid[0][x] == 2:
                return 2
            elif grid[0][x] == 0:
                return grid[0][x]
    # diagonals
    diag1 = set([grid[0][0],    grid[1][1], grid[2][2]])
    diag2 = set([grid[0][2],    grid[1][1], grid[2][0]])
    if len(diag1) == 1 or len(diag2) == 1 and grid[1][1] != 0:
        if grid[1][1] == 1:
            return 1
        elif grid[1][1] == 2:
            return 2
        elif grid[1][1] == 0:
            return -1
    
    return -1


if __name__ == "__main__":
    print(is_solved([[2, 1, 2], [2, 1, 1], [1, 2, 1]]))