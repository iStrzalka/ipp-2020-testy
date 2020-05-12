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
uuid: 759027974
"""
"""
random actions, total chaos
"""
board = gamma_new(7, 6, 5, 3)
assert board is not None


assert gamma_move(board, 1, 2, 2) == 1 
assert gamma_move(board, 1, 0, 1) == 1 
assert gamma_move(board, 2, 2, 4) == 1 
assert gamma_move(board, 2, 2, 5) == 1 
assert gamma_move(board, 3, 0, 0) == 1 
assert gamma_move(board, 3, 3, 0) == 1 
assert gamma_golden_possible(board, 3) == 1 
assert gamma_move(board, 4, 0, 4) == 1 
assert gamma_move(board, 5, 3, 2) == 1 
assert gamma_move(board, 5, 6, 5) == 1 
assert gamma_golden_move(board, 5, 1, 0) == 0 
assert gamma_move(board, 1, 1, 1) == 1 
assert gamma_move(board, 1, 0, 1) == 0 
assert gamma_free_fields(board, 1) == 32 
assert gamma_move(board, 2, 1, 2) == 1 
assert gamma_free_fields(board, 2) == 31 
assert gamma_move(board, 3, 3, 3) == 1 
assert gamma_move(board, 3, 2, 3) == 1 
assert gamma_move(board, 4, 2, 3) == 0 
assert gamma_busy_fields(board, 4) == 1 
assert gamma_move(board, 5, 2, 6) == 0 
assert gamma_move(board, 5, 0, 5) == 1 
assert gamma_move(board, 1, 3, 5) == 1 
assert gamma_move(board, 1, 4, 1) == 0 
assert gamma_busy_fields(board, 1) == 4 
assert gamma_move(board, 2, 1, 3) == 1 
assert gamma_move(board, 2, 3, 1) == 1 
assert gamma_move(board, 3, 3, 0) == 0 
assert gamma_move(board, 3, 2, 2) == 0 
assert gamma_move(board, 4, 4, 1) == 1 
assert gamma_move(board, 5, 3, 6) == 0 
assert gamma_move(board, 5, 2, 3) == 0 
assert gamma_move(board, 1, 2, 3) == 0 
assert gamma_free_fields(board, 1) == 5 
assert gamma_move(board, 2, 5, 4) == 0 
assert gamma_move(board, 3, 3, 6) == 0 
assert gamma_move(board, 3, 5, 3) == 0 
assert gamma_golden_move(board, 3, 4, 0) == 0 
assert gamma_move(board, 5, 3, 0) == 0 
assert gamma_move(board, 5, 2, 0) == 0 
assert gamma_move(board, 1, 1, 0) == 1 
assert gamma_move(board, 2, 0, 6) == 0 
assert gamma_move(board, 2, 1, 0) == 0 
assert gamma_move(board, 3, 3, 0) == 0 
assert gamma_move(board, 4, 3, 4) == 1 
assert gamma_move(board, 4, 5, 2) == 0 
assert gamma_move(board, 5, 1, 5) == 1 
assert gamma_golden_possible(board, 5) == 1 
assert gamma_move(board, 1, 4, 4) == 0 
assert gamma_move(board, 1, 5, 0) == 0 
assert gamma_move(board, 2, 0, 5) == 0 
assert gamma_move(board, 3, 1, 4) == 0 
assert gamma_move(board, 3, 0, 2) == 0 
assert gamma_move(board, 4, 2, 4) == 0 
assert gamma_golden_possible(board, 4) == 1 
assert gamma_move(board, 5, 3, 1) == 0 
assert gamma_move(board, 5, 5, 1) == 0 
assert gamma_move(board, 1, 1, 3) == 0 
assert gamma_move(board, 1, 0, 2) == 1 
assert gamma_golden_possible(board, 1) == 1 


board859215437 = gamma_board(board)
assert board859215437 is not None
assert board859215437 == ("5521..5\n"
"4.24...\n"
".233...\n"
"1215...\n"
"11.24..\n"
"31.3...\n")
del board859215437
board859215437 = None
assert gamma_move(board, 2, 4, 4) == 0 
assert gamma_free_fields(board, 2) == 3 
assert gamma_move(board, 3, 1, 5) == 0 
assert gamma_move(board, 4, 2, 4) == 0 
assert gamma_move(board, 5, 6, 0) == 0 
assert gamma_move(board, 5, 1, 4) == 1 
assert gamma_free_fields(board, 5) == 3 
assert gamma_golden_possible(board, 5) == 1 
assert gamma_move(board, 1, 2, 2) == 0 
assert gamma_move(board, 1, 6, 3) == 0 
assert gamma_move(board, 3, 3, 1) == 0 
assert gamma_move(board, 3, 5, 4) == 0 
assert gamma_move(board, 4, 2, 4) == 0 
assert gamma_move(board, 4, 2, 2) == 0 
assert gamma_free_fields(board, 4) == 5 
assert gamma_move(board, 5, 4, 4) == 0 
assert gamma_move(board, 5, 2, 1) == 0 
assert gamma_move(board, 1, 3, 0) == 0 
assert gamma_free_fields(board, 1) == 4 
assert gamma_move(board, 2, 5, 5) == 0 
assert gamma_move(board, 3, 0, 5) == 0 
assert gamma_move(board, 3, 4, 4) == 0 
assert gamma_busy_fields(board, 3) == 4 
assert gamma_move(board, 4, 4, 5) == 0 
assert gamma_move(board, 5, 2, 0) == 0 
assert gamma_move(board, 1, 0, 1) == 0 
assert gamma_busy_fields(board, 1) == 6 
assert gamma_golden_possible(board, 1) == 1 
assert gamma_move(board, 2, 4, 6) == 0 
assert gamma_move(board, 3, 0, 4) == 0 
assert gamma_free_fields(board, 3) == 3 
assert gamma_golden_possible(board, 3) == 1 
assert gamma_move(board, 4, 0, 6) == 0 
assert gamma_move(board, 1, 3, 4) == 0 
assert gamma_move(board, 2, 5, 4) == 0 
assert gamma_move(board, 2, 3, 1) == 0 
assert gamma_move(board, 3, 4, 0) == 1 
assert gamma_move(board, 4, 3, 6) == 0 
assert gamma_free_fields(board, 4) == 4 
assert gamma_move(board, 5, 3, 2) == 0 
assert gamma_move(board, 1, 6, 0) == 0 
assert gamma_move(board, 1, 3, 5) == 0 
assert gamma_move(board, 2, 3, 5) == 0 
assert gamma_busy_fields(board, 2) == 5 
assert gamma_free_fields(board, 2) == 2 
assert gamma_move(board, 3, 3, 1) == 0 
assert gamma_move(board, 4, 2, 6) == 0 
assert gamma_move(board, 4, 3, 5) == 0 
assert gamma_busy_fields(board, 4) == 3 
assert gamma_move(board, 2, 3, 5) == 0 
assert gamma_golden_move(board, 2, 4, 0) == 0 
assert gamma_move(board, 3, 4, 0) == 0 
assert gamma_move(board, 5, 1, 4) == 0 
assert gamma_move(board, 1, 3, 4) == 0 
assert gamma_move(board, 2, 4, 5) == 0 
assert gamma_move(board, 2, 1, 3) == 0 
assert gamma_move(board, 3, 3, 4) == 0 
assert gamma_move(board, 3, 3, 1) == 0 
assert gamma_golden_move(board, 3, 1, 4) == 0 
assert gamma_move(board, 4, 0, 5) == 0 
assert gamma_move(board, 5, 1, 6) == 0 
assert gamma_golden_possible(board, 5) == 1 
assert gamma_move(board, 1, 3, 0) == 0 
assert gamma_golden_possible(board, 1) == 1 
assert gamma_move(board, 2, 2, 6) == 0 
assert gamma_move(board, 2, 1, 2) == 0 
assert gamma_move(board, 3, 2, 2) == 0 
assert gamma_move(board, 4, 3, 6) == 0 
assert gamma_move(board, 4, 1, 1) == 0 
assert gamma_move(board, 5, 5, 2) == 0 
assert gamma_move(board, 5, 4, 4) == 0 
assert gamma_free_fields(board, 1) == 4 
assert gamma_move(board, 2, 1, 5) == 0 
assert gamma_free_fields(board, 2) == 2 
assert gamma_move(board, 3, 3, 6) == 0 
assert gamma_move(board, 4, 2, 4) == 0 
assert gamma_move(board, 4, 6, 2) == 0 
assert gamma_golden_move(board, 4, 3, 1) == 1 
assert gamma_move(board, 5, 1, 2) == 0 
assert gamma_free_fields(board, 5) == 3 
assert gamma_move(board, 2, 3, 3) == 0 
assert gamma_move(board, 2, 0, 4) == 0 
assert gamma_busy_fields(board, 3) == 5 
assert gamma_move(board, 4, 4, 5) == 0 
assert gamma_move(board, 4, 0, 2) == 0 


gamma_delete(board)