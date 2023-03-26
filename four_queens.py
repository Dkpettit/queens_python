import copy

#four_queesn.py
"""
Solve the Four Queens problem
on a 4 x 4 board, the objective to place 4 queens on a 4 x 4 chess board in a way that prevents each queen from attacking the others
"""

# a Queen
Q = True

B = False

# total number of indexes
available_positions = range(16)

"""
A Starting 4 x 4 board, all spaces available
"""
BD0 = [B, B, B, B,
       B, B, B, B,
       B, B, B, B,
       B, B, B, B,]

BD1 = [Q, B, B, B,
       B, B, B, B,
       B, B, B, B,
       B, B, B, B,]

BD2 = [Q, Q, B, B,
       B, Q, B, B,
       B, B, B, B,
       B, B, B, B,]

BD3 = [Q, B, B, B,
       B, B, Q, B,
       B, B, B, B,
       B, B, B, B,]

BD4 = [B, Q, B, B,
       B, B, B, Q,
       Q, B, B, B,
       B, B, Q, B,]

BD5 = [B, Q, B, B,
       B, B, B, B,
       Q, B, B, B,
       B, B, B, B,]

BD6 = [B, B, B, B,
       B, B, B, Q,
       B, B, B, B,
       B, B, B, B,]

BD7 = [B, B, B, B,
       B, B, B, B,
       B, B, B, B,
       B, B, Q, B,]

"""
Lists used to traverse the Board using indexes that represent Horizontal (Rows), Vertical(Columns), and Diagonal (diagonals)
"""
rows = [ [  0,  1,  2,  3 ],
         [  4,  5,  6,  7 ],
         [  8,  9, 10, 11 ],
         [ 12, 13, 14, 15 ] ]
 
columns = [ [ 0,  4,  8, 12 ],
            [ 1,  5,  9, 13 ],
            [ 2,  6, 10, 14 ],
            [ 3,  7, 11, 15 ] ]
 
diagonals = [ [  1,  4 ],
              [  2,  5,  8 ],
              [  3,  6,  9, 12 ],
              [  7, 10, 13 ],
              [ 11, 14 ],
              [  2,  7 ],
              [  1,  6, 11 ],
              [  0,  5, 10, 15 ],
              [  4,  9, 14 ],
              [  8, 13] ]


# Tests if the board is valid, does it have 4 queens positioned in a way that prevents them from attacking the others
# i.e. there is only one queen in each row, column and dagonal.
def is_board_valid(brd):
    def check_spaces(spaces):
        for space in spaces:
            if num_queens(brd, space) > 1:
                return False
        return True
    return all([check_spaces(x) for x in [rows, columns, diagonals]])

# Tests for queen (True)
def num_queens(brd, positions):
    return sum([ 1 for pos in positions if brd[pos] ])

# Has the board been solved -- The board is a list, is valid and there are 4 queens that meet the constraints
def is_board_solved(brd):
    return isinstance(brd, list) and is_board_valid(brd) and num_queens(brd, available_positions) == 4


# Get the available positions on the board
def get_available_positions(brd):
    return [x for x in range(len(brd)) if not brd[x]]

# Test the board
def get_next(brd, positions):
    result = []    

    for pos in positions:
        temp = copy.deepcopy(brd)
        temp[pos] = True
        result.append(temp)

    return [board for board in result if is_board_valid(board) ]

def solve(brd):
    if is_board_solved(brd):
        return brd
    else:
        return solve_board_list(get_next(brd, get_available_positions(brd)))
    
def solve_board_list(brd_list):
    if brd_list == []:
        return False
    else:
        check = solve(brd_list[0])
        if is_board_solved(check) != False:
            return check
        else:
            return solve_board_list(brd_list[1:])
    


def visualize(board):
    """
    Input: valid board or False
    Output: string representing squares as "X" and "Q", or False
    """
    if not isinstance(board, list):
        return False
    
    res = ""
    for i in range(len(board)):
        if board[i]:
            res += "Q "
        else:
            res += "X "
        if (i + 1) % 4 == 0 and i < len(board) - 1:
            res += "\n"
    return res

# print(visualize(solve(BD2)))

#Test each board provided as test cases
assert solve(BD0) == BD4
assert solve(BD1) == False
assert solve(BD2) == False
assert solve(BD3) == False
assert solve(BD4) == BD4
assert solve(BD5) == BD4
assert solve(BD6) == BD4
assert solve(BD7) == BD4