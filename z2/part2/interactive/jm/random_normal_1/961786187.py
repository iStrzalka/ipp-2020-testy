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
uuid: 961786187
"""
"""
random actions, total chaos
"""
board = gamma_new(6, 5, 3, 13)
assert board is not None


assert gamma_move(board, 1, 3, 4) == 1 
assert gamma_busy_fields(board, 1) == 1 
assert gamma_golden_possible(board, 1) == 0 


board286061200 = gamma_board(board)
assert board286061200 is not None
assert board286061200 == ("...1..\n"
"......\n"
"......\n"
"......\n"
"......\n")
del board286061200
board286061200 = None
assert gamma_move(board, 2, 0, 5) == 0 
assert gamma_move(board, 3, 4, 5) == 0 
assert gamma_move(board, 3, 0, 3) == 1 
assert gamma_move(board, 1, 2, 4) == 1 
assert gamma_free_fields(board, 1) == 27 
assert gamma_move(board, 2, 3, 3) == 1 
assert gamma_move(board, 3, 0, 5) == 0 
assert gamma_move(board, 3, 5, 2) == 1 
assert gamma_busy_fields(board, 3) == 2 
assert gamma_move(board, 1, 3, 2) == 1 
assert gamma_move(board, 2, 3, 2) == 0 
assert gamma_move(board, 2, 3, 4) == 0 
assert gamma_move(board, 3, 4, 3) == 1 
assert gamma_move(board, 1, 0, 0) == 1 
assert gamma_free_fields(board, 1) == 22 
assert gamma_move(board, 2, 1, 0) == 1 
assert gamma_move(board, 2, 1, 1) == 1 
assert gamma_busy_fields(board, 2) == 3 
assert gamma_free_fields(board, 2) == 20 
assert gamma_golden_move(board, 3, 4, 3) == 0 
assert gamma_move(board, 1, 3, 4) == 0 
assert gamma_move(board, 1, 2, 1) == 1 
assert gamma_move(board, 2, 5, 0) == 1 
assert gamma_golden_move(board, 2, 4, 2) == 0 
assert gamma_move(board, 3, 2, 4) == 0 
assert gamma_move(board, 3, 3, 0) == 1 
assert gamma_busy_fields(board, 3) == 4 
assert gamma_move(board, 1, 1, 5) == 0 
assert gamma_move(board, 1, 4, 0) == 1 
assert gamma_move(board, 2, 3, 5) == 0 
assert gamma_move(board, 2, 5, 1) == 1 
assert gamma_golden_move(board, 2, 2, 3) == 0 
assert gamma_move(board, 3, 4, 1) == 1 
assert gamma_move(board, 3, 4, 2) == 1 
assert gamma_move(board, 1, 4, 0) == 0 
assert gamma_move(board, 1, 2, 2) == 1 
assert gamma_move(board, 2, 4, 5) == 0 
assert gamma_move(board, 3, 4, 4) == 1 
assert gamma_move(board, 3, 2, 4) == 0 
assert gamma_golden_move(board, 3, 0, 4) == 0 
assert gamma_move(board, 1, 4, 0) == 0 
assert gamma_move(board, 1, 4, 0) == 0 
assert gamma_move(board, 2, 0, 2) == 1 
assert gamma_move(board, 2, 4, 1) == 0 
assert gamma_move(board, 3, 3, 5) == 0 
assert gamma_move(board, 3, 1, 3) == 1 
assert gamma_golden_possible(board, 3) == 1 
assert gamma_move(board, 1, 1, 3) == 0 
assert gamma_golden_possible(board, 1) == 1 
assert gamma_move(board, 2, 0, 0) == 0 
assert gamma_move(board, 2, 1, 1) == 0 
assert gamma_free_fields(board, 2) == 9 
assert gamma_move(board, 3, 1, 3) == 0 
assert gamma_move(board, 3, 4, 2) == 0 
assert gamma_free_fields(board, 3) == 9 
assert gamma_move(board, 1, 3, 5) == 0 
assert gamma_move(board, 2, 2, 0) == 1 
assert gamma_free_fields(board, 2) == 8 
assert gamma_move(board, 3, 4, 3) == 0 
assert gamma_busy_fields(board, 3) == 8 
assert gamma_move(board, 1, 3, 0) == 0 
assert gamma_move(board, 2, 0, 2) == 0 
assert gamma_move(board, 2, 3, 3) == 0 
assert gamma_move(board, 3, 5, 3) == 1 
assert gamma_move(board, 1, 3, 2) == 0 
assert gamma_free_fields(board, 1) == 7 
assert gamma_move(board, 2, 5, 1) == 0 
assert gamma_move(board, 2, 4, 1) == 0 
assert gamma_golden_possible(board, 2) == 1 
assert gamma_move(board, 3, 4, 1) == 0 
assert gamma_move(board, 3, 0, 4) == 1 


board387269707 = gamma_board(board)
assert board387269707 is not None
assert board387269707 == ("3.113.\n"
"33.233\n"
"2.1133\n"
".21.32\n"
"122312\n")
del board387269707
board387269707 = None
assert gamma_move(board, 1, 1, 3) == 0 
assert gamma_move(board, 2, 4, 0) == 0 
assert gamma_move(board, 2, 0, 2) == 0 
assert gamma_move(board, 3, 1, 4) == 1 
assert gamma_busy_fields(board, 1) == 7 
assert gamma_move(board, 2, 3, 2) == 0 
assert gamma_move(board, 2, 5, 3) == 0 
assert gamma_move(board, 3, 2, 1) == 0 
assert gamma_move(board, 3, 2, 2) == 0 
assert gamma_golden_move(board, 3, 0, 5) == 0 
assert gamma_move(board, 1, 1, 0) == 0 
assert gamma_move(board, 2, 3, 2) == 0 
assert gamma_move(board, 2, 2, 2) == 0 
assert gamma_free_fields(board, 2) == 5 
assert gamma_move(board, 3, 5, 2) == 0 
assert gamma_move(board, 3, 4, 2) == 0 
assert gamma_move(board, 1, 4, 5) == 0 
assert gamma_move(board, 1, 4, 4) == 0 
assert gamma_golden_move(board, 1, 1, 4) == 1 
assert gamma_move(board, 2, 1, 3) == 0 
assert gamma_move(board, 2, 2, 1) == 0 
assert gamma_busy_fields(board, 2) == 7 
assert gamma_move(board, 3, 5, 4) == 1 
assert gamma_busy_fields(board, 3) == 11 
assert gamma_free_fields(board, 3) == 4 
assert gamma_move(board, 1, 1, 1) == 0 
assert gamma_move(board, 2, 3, 2) == 0 
assert gamma_move(board, 2, 3, 1) == 1 
assert gamma_busy_fields(board, 2) == 8 
assert gamma_move(board, 3, 1, 0) == 0 
assert gamma_free_fields(board, 3) == 3 
assert gamma_move(board, 1, 2, 0) == 0 
assert gamma_move(board, 1, 5, 2) == 0 
assert gamma_busy_fields(board, 1) == 8 
assert gamma_move(board, 2, 5, 0) == 0 
assert gamma_move(board, 2, 0, 1) == 1 
assert gamma_move(board, 3, 5, 3) == 0 
assert gamma_move(board, 3, 5, 4) == 0 
assert gamma_move(board, 1, 0, 2) == 0 
assert gamma_busy_fields(board, 1) == 8 
assert gamma_move(board, 2, 2, 1) == 0 
assert gamma_move(board, 3, 2, 1) == 0 
assert gamma_move(board, 1, 3, 2) == 0 
assert gamma_busy_fields(board, 1) == 8 
assert gamma_move(board, 2, 0, 1) == 0 
assert gamma_busy_fields(board, 2) == 9 
assert gamma_move(board, 3, 2, 1) == 0 
assert gamma_move(board, 3, 2, 1) == 0 
assert gamma_free_fields(board, 3) == 2 
assert gamma_golden_move(board, 3, 1, 5) == 0 


gamma_delete(board)
