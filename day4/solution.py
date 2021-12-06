from typing import List


def create_bingo_boards(bingo_inputs: list):
    board = []
    bingo_boards = []

    numbers_to_draw = bingo_inputs[0].rstrip().split(',')
    numbers_to_draw = list(map(int, numbers_to_draw))
    del bingo_inputs[0]
    del bingo_inputs[0]

    for line in bingo_inputs:
        board_line = line.rstrip().split(' ')
        while '' in board_line:
            board_line.remove('')
        board_line = list(map(int, board_line))
        if len(board_line) == 0:
            bingo_boards.append(board)
            board = []
            continue
        board.append(board_line)
    
    bingo_boards.append(board)
    return numbers_to_draw, bingo_boards

def mark_board(board: List[list], number: int) -> list:
    for line in board:
        if number in line:
            pos = line.index(number)
            line[pos] = -1
    return board

def check_board(board: List[list]) -> bool:
    winner = False
    for line in board:
        if sum(line) == -5:
            winner = True
            break
    # Check on vertical
    for i in range(5):
        column_sum = 0
        for line in board:
            column_sum += line[i]
            if column_sum == -5:
                winner = True
                
        if winner:
            break
    return winner

def calculate_score(board: List[list], last_number_called: int):
    score = 0
    for line in board:
        score += sum(line)
    return score * last_number_called

def main():
    winning_board: List[list] = []
    last_number_called = None

    with open("input.csv") as inputs:
        bingo_inputs = list(inputs)

    numbers, boards = create_bingo_boards(bingo_inputs)

    for number in numbers:
        for board in boards:
            board = mark_board(board, number)
            winner = check_board(board)
            if winner:
                winning_board = board
                break
        if winning_board != []:
            last_number_called = number
            break
    for line in winning_board:
        while -1 in line:
            line.remove(-1)
    final_score = calculate_score(winning_board, last_number_called)
    print(f"Final Score: {final_score}")
    

if __name__ == "__main__":
    main()