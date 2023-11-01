"""Puzzle module https://github.com/senivan/Sen-Ivan-lab8-task2"""
def validate_board(board):
    '''
        Function that validates the board
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
    pass

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())