board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

def isValidSudoku(board):
        # rows
        seen = {}
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue

                if board[i][j] not in seen:
                    seen[board[i][j]] = True
                else:
                    #print("rows false")
                    return False
            
            seen = {}

        # columns
        for i in range(9):
            for j in range(9):
                if board[j][i] == ".":
                    continue

                if board[j][i] not in seen:
                    seen[board[j][i]] = True
                else:
                    #print("cols false")
                    return False
            seen = {}
        
        # sub-boxes
        def sub_box(start_i, start_j):
            seen = {}
            for i in range(start_i, start_i + 3):  
                for j in range(start_j, start_j + 3):
                    if board[i][j] == ".":
                        continue
                    if board[i][j] not in seen:
                        seen[board[i][j]] = True
                    else:
                        #print(f"box false: {start_i} to {start_i + 3} / {start_j} to {start_j + 3}")
                        return False
            return True

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not sub_box(i, j):
                    return False

        return True


print(isValidSudoku(board))