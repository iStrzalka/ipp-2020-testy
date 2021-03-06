from part1 import (
    gamma_board,
    gamma_busy_fields,
    gamma_delete,
    gamma_free_fields,
    gamma_golden_move,
    gamma_golden_possible,
    gamma_move,
    gamma_new,
)

"""
scenario: test_random_actions
uuid: 800086241
"""
"""
random actions, total chaos
"""
board = gamma_new(5, 5, 5, 6)
assert board is not None


assert gamma_free_fields(board, 1) == 25 
assert gamma_move(board, 2, 2, 1) == 1 
assert gamma_move(board, 3, 2, 3) == 1 
assert gamma_move(board, 5, 1, 4) == 1 
assert gamma_move(board, 1, 4, 2) == 1 
assert gamma_move(board, 2, 0, 4) == 1 
assert gamma_move(board, 2, 2, 2) == 1 
assert gamma_move(board, 3, 0, 2) == 1 
assert gamma_move(board, 3, 0, 1) == 1 
assert gamma_golden_move(board, 3, 4, 1) == 0 
assert gamma_move(board, 4, 1, 0) == 1 
assert gamma_move(board, 5, 0, 4) == 0 
assert gamma_busy_fields(board, 5) == 1 
assert gamma_move(board, 1, 4, 4) == 1 
assert gamma_golden_move(board, 1, 2, 0) == 0 
assert gamma_move(board, 2, 0, 4) == 0 
assert gamma_move(board, 2, 2, 2) == 0 
assert gamma_move(board, 3, 1, 4) == 0 
assert gamma_move(board, 3, 2, 1) == 0 
assert gamma_move(board, 4, 2, 1) == 0 
assert gamma_move(board, 4, 0, 1) == 0 
assert gamma_move(board, 5, 2, 0) == 1 
assert gamma_move(board, 5, 2, 0) == 0 
assert gamma_move(board, 1, 3, 1) == 1 
assert gamma_move(board, 2, 1, 0) == 0 
assert gamma_move(board, 2, 3, 1) == 0 
assert gamma_free_fields(board, 2) == 13 
assert gamma_move(board, 3, 0, 3) == 1 
assert gamma_move(board, 5, 4, 3) == 1 
assert gamma_move(board, 5, 3, 2) == 1 
assert gamma_move(board, 1, 4, 1) == 1 
assert gamma_move(board, 3, 2, 1) == 0 
assert gamma_move(board, 3, 3, 2) == 0 
assert gamma_busy_fields(board, 3) == 4 
assert gamma_move(board, 4, 0, 2) == 0 
assert gamma_move(board, 4, 4, 2) == 0 
assert gamma_move(board, 5, 0, 0) == 1 
assert gamma_move(board, 5, 2, 0) == 0 
assert gamma_move(board, 1, 3, 0) == 1 
assert gamma_move(board, 2, 1, 1) == 1 
assert gamma_move(board, 2, 1, 1) == 0 
assert gamma_free_fields(board, 2) == 6 
assert gamma_move(board, 4, 4, 2) == 0 
assert gamma_move(board, 4, 3, 3) == 1 
assert gamma_move(board, 5, 2, 1) == 0 
assert gamma_free_fields(board, 5) == 5 
assert gamma_move(board, 1, 2, 1) == 0 
assert gamma_move(board, 2, 0, 4) == 0 
assert gamma_busy_fields(board, 2) == 4 
assert gamma_move(board, 3, 2, 1) == 0 
assert gamma_move(board, 4, 1, 0) == 0 
assert gamma_move(board, 5, 4, 2) == 0 
assert gamma_move(board, 5, 2, 0) == 0 
assert gamma_move(board, 1, 4, 2) == 0 
assert gamma_move(board, 1, 4, 4) == 0 
assert gamma_busy_fields(board, 1) == 5 
assert gamma_move(board, 2, 4, 2) == 0 
assert gamma_move(board, 2, 1, 0) == 0 
assert gamma_move(board, 4, 1, 1) == 0 
assert gamma_move(board, 5, 3, 1) == 0 
assert gamma_move(board, 2, 4, 4) == 0 
assert gamma_move(board, 2, 2, 2) == 0 
assert gamma_move(board, 3, 4, 3) == 0 
assert gamma_move(board, 4, 0, 3) == 0 
assert gamma_busy_fields(board, 4) == 2 
assert gamma_move(board, 5, 3, 0) == 0 
assert gamma_move(board, 5, 1, 0) == 0 
assert gamma_golden_move(board, 5, 0, 3) == 1 
assert gamma_move(board, 1, 4, 2) == 0 
assert gamma_move(board, 1, 2, 4) == 1 
assert gamma_move(board, 2, 4, 3) == 0 
assert gamma_move(board, 2, 3, 1) == 0 
assert gamma_busy_fields(board, 2) == 4 
assert gamma_move(board, 3, 1, 4) == 0 
assert gamma_move(board, 4, 0, 4) == 0 
assert gamma_move(board, 4, 2, 1) == 0 
assert gamma_free_fields(board, 4) == 4 
assert gamma_move(board, 5, 4, 3) == 0 


gamma_delete(board)
