

for _ in xrange(int(raw_input())):
    board = []
    count = 0
    pos = []
    winnable = 'NO'
    for i in range(4):
        rows = [i for i in raw_input()]
        board.append(rows)

    for row in board:
        print " ".join(row)

    for row in board:
        for place in row:
            if place == 'x' or place == 'o':
                count += 1

    if count == 0:
        print winnable

    if count % 2 == 0:
        bat_piece = 'x'
    else:
        bat_piece = 'o'

    for row in range(0,4):
        for col in range(0,4):
            if board[row][col] == bat_piece:
                pos.append((row, col))

    print pos

    for positions in pos:
        row_1, col_1 = positions
        if winnable == 'YES':
            break
        #right_row
        if col_1 + 1 in range(0,4) and col_1 + 2 in range(0,4):
            if board[row_1][col_1 + 1] == bat_piece and board[row_1][col_1 + 2] == '.':
                winnable = 'YES'
                
            elif board[row_1][col_1 + 1] == '.' and board[row_1][col_1 + 2] == bat_piece:
                winnable = 'YES'
                

        #left_row
        elif col_1 - 1 in range(0,4) and col_1 - 2 in range(0,4):
            if board[row_1][col_1 - 1] == bat_piece and board[row_1][col_1 - 2] == '.':
                winnable = 'YES'
                
            elif board[row_1][col_1 - 1] == '.' and board[row_1][col_1 - 2] == bat_piece:
                winnable = 'YES'
                

        #below
        elif row_1 + 1 in range(0,4) and row_1 + 2 in range(0,4):
            if board[row_1 + 1][col_1] == bat_piece and board[row_1 + 2][col_1] == '.':
                winnable = 'YES'
                
            elif board[row_1 + 1][col_1] == '.' and board[row_1 + 2][col_1] == bat_piece:
                winnable = 'YES'
                

        #above
        elif row_1 - 1 in range(0,4) and row_1 - 2 in range(0,4):
            if board[row_1 - 1][col_1] == bat_piece and board[row_1 - 2][col_1] == '.':
                winnable = 'YES'
                
            if board[row_1 - 1][col_1] == '.' and board[row_1 - 2][col_1] == bat_piece:
                winnable = 'YES'
                

        #left_diagonal
        elif row_1 - 1 in range(0,4) and col_1 - 1 in range(0,4):
            if board[row_1 - 1][col_1 - 1] == bat_piece and board[row_1 + 1][col_1 + 1] == '.':
                winnable = 'YES'
                
            elif board[row_1 - 1][col_1 - 1] == '.' and board[row_1 + 1][col_1 + 1] == bat_piece:
                winnable = 'YES'
                
        #left_diagonal
        elif row_1 - 1 in range(0, 4) and col_1 - 1 in range(0, 4):
            if row_1 - 2 in range(0, 4) and col_1 - 2 in range(0, 4):
                if board[row_1 - 1][col_1 - 1] == bat_piece and board[row_1 - 2][col_1 -2] == '.':
                    winnable = 'YES'
                    
                elif board[row_1 - 1][col_1 - 1] == '.' and board[row_1 - 2][col_1 - 2] == bat_piece:
                    winnable = 'YES'
                    


        #right_diagonal
        elif row_1 - 1 in range(0,4) and col_1 + 1 in range(0,4):
            if board[row_1 - 1][col_1 + 1] == bat_piece and board[row_1 + 1][col_1 - 1] == '.':
                winnable = 'YES'
                
            elif board[row_1 - 1][col_1 + 1] == '.' and board[row_1 + 1][col_1 - 1] == bat_piece:
                winnable = 'YES'
                
        #right_diagonal
        elif row_1 - 1 in range(0, 4) and col_1 + 1 in range(0, 4):
            if row_1 - 2 in range(0, 4) and col_1 + 2 in range(0, 4):
                if board[row_1 - 1][col_1 + 1] == bat_piece and board[row_1 - 2][col_1 + 2] == '.':
                    winnable = 'YES'
                    
                elif board[row_1 - 1][col_1 + 1] == '.' and board[row_1 - 2][col_1 + 2] == bat_piece:
                    winnable = 'YES'
                    

        #left_below_diagonal
        elif row_1 + 1 in range(0,4) and col_1 - 1 in range(0,4):
            if board[row_1 + 1][col_1 - 1] == bat_piece and board[row_1 - 1][col_1 + 1] == '.':
                winnable = 'YES'
                
            elif board[row_1 + 1][col_1 - 1] == '.' and board[row_1 - 1][col_1 + 1] == bat_piece:
                winnable = 'YES'
                
        #left_below_diagonal
        elif row_1 + 1 in range(0, 4) and col_1 - 1 in range(0, 4):
            if row_1 + 2 in range(0, 4) and col_1 - 2 in range(0, 4):
                if board[row_1 + 1][col_1 - 1] == bat_piece and board[row_1 + 2][col_1 - 2] == '.':
                    winnable = 'YES'
                    
                elif board[row_1 + 1][col_1 - 1] == '.' and board[row_1 + 2][col_1 - 2] == bat_piece:
                    winnable = 'YES'
                    

        #right_below_diagonal
        elif row_1 + 1 in range(0,4) and col_1 + 1 in range(0,4):
            if board[row_1 + 1][col_1 + 1] == bat_piece and board[row_1 - 1][col_1 - 1] == '.':
                winnable = 'YES'
                
            elif board[row_1 + 1][col_1 + 1] == '.' and board[row_1 - 1][col_1 - 1] == bat_piece:
                winnable = 'YES'
                
        #right_below_diagonal
        elif row_1 + 1 in range(0, 4) and col_1 + 1 in range(0, 4) and row_1 + 2 in range(0, 4) and col_1 + 2 in range(0, 4):
                if board[row_1 + 1][col_1 + 1] == bat_piece and board[row_1 + 2][col_1 + 2] == '.':
                    print 'YES'
                    
                elif board[row_1 + 1][col_1 + 1] == '.' and board[row_1 + 2][col_1 + 2] == bat_piece:
                    print 'YES'
                    

    #print winnable

'''if row_1 + 2 in range(0, 4) and col_1 + 2 in range(0, 4):'''











