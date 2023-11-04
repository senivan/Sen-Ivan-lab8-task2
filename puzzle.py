"""Puzzle module https://github.com/senivan/Sen-Ivan-lab8-task2"""

def check_horizontal(board:list[str])->bool:
    '''
    Function that checks horizontal lines of board
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
    >>> check_horizontal(board)
    True
    '''
    for line in board:
        for lt in line:
            if lt != '*' and lt != ' ' and line.count(lt) > 1:
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
        for lt in line:
            if lt != '*' and lt != ' ' and line.count(lt) > 1:
                return False
    return True

def check_color(board:list[str]) -> bool:
    '''
    Function that checks color lines of board
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
    >>> check_color(board) 
    True
    '''
    board_rotate = []
    for i, _ in enumerate(board):
        line = []
        for j in board:
            line.append(j[i])
        board_rotate.append(line)
    test_lines = []
    hor_index = 8
    ver_index = 0
    for i in range(6):
        line = []
        line += ''.join(board_rotate[ver_index][:len(board)-i]) + ''.join(board[hor_index][i+1:])
        ver_index+=1
        hor_index-=1
        test_lines.append(line)

    for line in test_lines:
        for lt in line:
            if lt != '*' and lt != ' ' and line.count(lt) > 1:
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
    return check_horizontal(board) and check_vertical(board) and check_color(board)

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
