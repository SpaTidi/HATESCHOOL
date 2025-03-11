from typing import List

def tic_tac_toe_checker(board: List[List]) -> str:
    lines = []
    counter = 0
    for i in range(3):
        lines.append(board[i])
        lines.append([board[0][i], board[1][i], board[2][i]])
    
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])
    
    for line in lines:
        if line[0] == line[1] == line[2] and line[0] != '-':
            counter += 1
            if counter > 1:
                raise ValueError("Некорректная доска")
    if counter == 1:
        return f"'{line[0].upper()}' победил!"

    if any('-' in row for row in board):
        return "Незаконченная игра"
    
    return "Ничья"


board1 = [
    ['x', 'x', 'x'],
    ['x', 'x', 'x'],
    ['x', 'o', 'x']
]
try:
    print(tic_tac_toe_checker(board1))
except Exception as e: 
    print(e)

board2 = [
    ['-', '-', 'o'],
    ['-', 'o', 'o'],
    ['x', 'x', 'x']
]
try:
    print(tic_tac_toe_checker(board2))
except Exception as e: 
    print(e)