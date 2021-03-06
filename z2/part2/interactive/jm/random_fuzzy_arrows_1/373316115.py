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
uuid: 373316115
"""
"""
random actions, total chaos
"""
board = gamma_new(8, 4, 5, 2)
assert board is not None


assert gamma_move(board, 1, 0, 6) == 0 
assert gamma_move(board, 2, 0, 4) == 0 
assert gamma_move(board, 3, 3, 6) == 0 
assert gamma_move(board, 4, 3, 1) == 1 
assert gamma_move(board, 5, 2, 3) == 1 
assert gamma_move(board, 5, 0, 2) == 1 
assert gamma_move(board, 1, 0, 4) == 0 
assert gamma_free_fields(board, 1) == 29 
assert gamma_move(board, 2, 1, 2) == 1 
assert gamma_move(board, 2, 7, 2) == 1 
assert gamma_move(board, 3, 0, 1) == 1 
assert gamma_move(board, 3, 5, 0) == 1 
assert gamma_move(board, 4, 0, 0) == 1 
assert gamma_move(board, 5, 0, 3) == 1 
assert gamma_move(board, 5, 1, 3) == 1 
assert gamma_move(board, 1, 7, 3) == 1 
assert gamma_move(board, 2, 0, 4) == 0 
assert gamma_move(board, 2, 6, 2) == 1 
assert gamma_move(board, 4, 1, 4) == 0 
assert gamma_move(board, 5, 0, 6) == 0 
assert gamma_move(board, 5, 6, 1) == 1 
assert gamma_busy_fields(board, 5) == 5 
assert gamma_move(board, 1, 3, 1) == 0 
assert gamma_move(board, 2, 1, 5) == 0 
assert gamma_move(board, 2, 0, 1) == 0 
assert gamma_move(board, 3, 3, 3) == 0 
assert gamma_golden_possible(board, 4) == 1 
assert gamma_move(board, 5, 4, 0) == 0 
assert gamma_busy_fields(board, 5) == 5 
assert gamma_move(board, 1, 2, 3) == 0 
assert gamma_move(board, 1, 2, 3) == 0 
assert gamma_move(board, 2, 3, 6) == 0 
assert gamma_move(board, 2, 2, 3) == 0 
assert gamma_busy_fields(board, 2) == 3 
assert gamma_move(board, 3, 0, 4) == 0 
assert gamma_move(board, 4, 5, 3) == 0 
assert gamma_move(board, 4, 0, 1) == 0 
assert gamma_move(board, 5, 2, 3) == 0 
assert gamma_move(board, 5, 5, 1) == 1 
assert gamma_move(board, 1, 5, 1) == 0 


board720057731 = gamma_board(board)
assert board720057731 is not None
assert board720057731 == ("555....1\n"
"52....22\n"
"3..4.55.\n"
"4....3..\n")
del board720057731
board720057731 = None
assert gamma_move(board, 2, 1, 2) == 0 
assert gamma_move(board, 2, 0, 2) == 0 
assert gamma_move(board, 3, 0, 3) == 0 
assert gamma_move(board, 4, 2, 3) == 0 
assert gamma_move(board, 4, 7, 1) == 0 
assert gamma_move(board, 5, 1, 4) == 0 
assert gamma_move(board, 1, 0, 3) == 0 
assert gamma_move(board, 1, 3, 0) == 1 
assert gamma_move(board, 2, 2, 5) == 0 
assert gamma_move(board, 2, 5, 3) == 0 
assert gamma_move(board, 3, 6, 2) == 0 
assert gamma_move(board, 4, 3, 2) == 1 
assert gamma_move(board, 5, 1, 4) == 0 
assert gamma_move(board, 5, 1, 3) == 0 
assert gamma_move(board, 1, 1, 1) == 0 
assert gamma_move(board, 2, 0, 1) == 0 
assert gamma_move(board, 2, 7, 1) == 1 
assert gamma_move(board, 3, 0, 7) == 0 
assert gamma_move(board, 5, 1, 2) == 0 
assert gamma_move(board, 5, 4, 3) == 0 
assert gamma_move(board, 2, 4, 0) == 0 
assert gamma_busy_fields(board, 2) == 4 
assert gamma_move(board, 3, 1, 1) == 1 
assert gamma_move(board, 3, 7, 0) == 0 
assert gamma_move(board, 4, 5, 0) == 0 
assert gamma_move(board, 5, 0, 2) == 0 
assert gamma_move(board, 5, 1, 0) == 0 
assert gamma_move(board, 1, 2, 4) == 0 
assert gamma_move(board, 1, 7, 0) == 0 
assert gamma_move(board, 2, 1, 4) == 0 
assert gamma_move(board, 2, 0, 0) == 0 
assert gamma_move(board, 4, 3, 6) == 0 
assert gamma_move(board, 5, 1, 1) == 0 
assert gamma_busy_fields(board, 5) == 6 
assert gamma_move(board, 1, 0, 1) == 0 
assert gamma_free_fields(board, 1) == 3 
assert gamma_move(board, 3, 1, 4) == 0 
assert gamma_move(board, 4, 7, 3) == 0 
assert gamma_move(board, 5, 0, 7) == 0 
assert gamma_move(board, 5, 4, 1) == 1 
assert gamma_golden_possible(board, 5) == 1 
assert gamma_move(board, 1, 2, 3) == 0 
assert gamma_free_fields(board, 1) == 3 
assert gamma_move(board, 2, 6, 0) == 0 
assert gamma_move(board, 3, 0, 4) == 0 
assert gamma_move(board, 4, 3, 6) == 0 
assert gamma_move(board, 4, 5, 1) == 0 
assert gamma_move(board, 1, 3, 4) == 0 
assert gamma_move(board, 1, 5, 2) == 0 
assert gamma_move(board, 2, 4, 0) == 0 
assert gamma_move(board, 2, 7, 2) == 0 
assert gamma_move(board, 3, 0, 4) == 0 
assert gamma_move(board, 4, 5, 0) == 0 


gamma_delete(board)
