"""Puzzle module https://github.com/senivan/Sen-Ivan-lab8-task2"""

def check_horizontal(board:list[str])->bool:
    '''
    Function that checks horizontal lines of board
    
    '''
    for line in board:
        if len(set(line)) != len(line):
            return False
    return True

def check_vertical(board:list[str])->bool:
    '''
    Function that checks vertical lines of board
    >>> board = [\
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"]
    >>> check_vertical(board)
    False
    '''
    for i in range(len(board)):
        line = [board[j][i] for j in range(len(board))]
        if len(set(line)) != len(line):
            return False
    return True

def validate_board(board:list[str]) -> bool:
    '''
    Function that validates board
    >>> board = [\
 "**** ****",\
 "***1 ****",\
 "**  3****",\
 "* 4 1****",\
 "     9 5 ",\
 " 6  83  *",\
 "3   1  **",\
 "  8  2***",\
 "  2  ****"]
    >>> validate_board(board)
    False
    '''


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())