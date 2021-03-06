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
uuid: 655765108
"""
"""
random actions, total chaos
"""
board = gamma_new(4, 4, 4, 2)
assert board is not None


assert gamma_move(board, 1, 0, 3) == 1 
assert gamma_move(board, 2, 2, 2) == 1 
assert gamma_move(board, 2, 0, 2) == 1 
assert gamma_busy_fields(board, 2) == 2 
assert gamma_move(board, 3, 3, 2) == 1 
assert gamma_busy_fields(board, 3) == 1 
assert gamma_move(board, 4, 2, 1) == 1 
assert gamma_move(board, 4, 0, 3) == 0 
assert gamma_free_fields(board, 1) == 11 
assert gamma_move(board, 2, 1, 0) == 0 
assert gamma_free_fields(board, 2) == 3 
assert gamma_move(board, 3, 0, 2) == 0 
assert gamma_free_fields(board, 3) == 11 
assert gamma_move(board, 4, 0, 0) == 1 
assert gamma_busy_fields(board, 4) == 2 
assert gamma_golden_possible(board, 4) == 1 
assert gamma_move(board, 1, 1, 1) == 1 
assert gamma_move(board, 2, 2, 1) == 0 
assert gamma_move(board, 3, 0, 3) == 0 
assert gamma_move(board, 3, 1, 1) == 0 
assert gamma_golden_move(board, 3, 1, 2) == 0 
assert gamma_move(board, 4, 3, 1) == 1 
assert gamma_move(board, 4, 2, 2) == 0 
assert gamma_move(board, 1, 1, 0) == 1 
assert gamma_golden_move(board, 1, 0, 0) == 1 
assert gamma_move(board, 2, 1, 0) == 0 


board637223611 = gamma_board(board)
assert board637223611 is not None
assert board637223611 == ("1...\n"
"2.23\n"
".144\n"
"11..\n")
del board637223611
board637223611 = None
assert gamma_move(board, 3, 0, 2) == 0 
assert gamma_move(board, 3, 1, 3) == 1 
assert gamma_busy_fields(board, 3) == 2 
assert gamma_move(board, 4, 2, 3) == 1 
assert gamma_move(board, 4, 2, 3) == 0 
assert gamma_free_fields(board, 4) == 3 


board854329175 = gamma_board(board)
assert board854329175 is not None
assert board854329175 == ("134.\n"
"2.23\n"
".144\n"
"11..\n")
del board854329175
board854329175 = None
assert gamma_move(board, 1, 2, 1) == 0 
assert gamma_move(board, 1, 2, 0) == 1 
assert gamma_move(board, 2, 0, 3) == 0 
assert gamma_move(board, 2, 3, 2) == 0 
assert gamma_move(board, 3, 1, 2) == 1 
assert gamma_move(board, 4, 1, 0) == 0 
assert gamma_move(board, 4, 2, 1) == 0 
assert gamma_move(board, 1, 0, 3) == 0 
assert gamma_free_fields(board, 1) == 2 
assert gamma_move(board, 2, 0, 3) == 0 
assert gamma_move(board, 2, 1, 3) == 0 
assert gamma_move(board, 3, 2, 2) == 0 
assert gamma_free_fields(board, 3) == 1 
assert gamma_golden_possible(board, 3) == 1 
assert gamma_move(board, 4, 0, 1) == 0 
assert gamma_move(board, 1, 3, 3) == 0 
assert gamma_move(board, 2, 3, 1) == 0 
assert gamma_move(board, 3, 1, 0) == 0 
assert gamma_move(board, 4, 0, 3) == 0 
assert gamma_move(board, 4, 3, 1) == 0 
assert gamma_move(board, 1, 1, 0) == 0 
assert gamma_move(board, 1, 3, 2) == 0 
assert gamma_move(board, 2, 0, 0) == 0 
assert gamma_move(board, 3, 0, 3) == 0 
assert gamma_move(board, 4, 3, 0) == 1 
assert gamma_free_fields(board, 4) == 1 


gamma_delete(board)
