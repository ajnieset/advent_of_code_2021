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
        if len(board_line) == 0:
            bingo_boards.append(board)
            board = []
            continue
        board.append(board_line)
    
    return numbers_to_draw, bingo_boards

def mark_board(board: list, number: int):
    pass

def main():
    with open("input.csv") as inputs:
        bingo_inputs = list(inputs)

    numbers, boards = create_bingo_boards(bingo_inputs)

if __name__ == "__main__":
    main()