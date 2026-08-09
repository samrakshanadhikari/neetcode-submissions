class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        # -------------------------
        # Check every row
        # -------------------------
        for i in range(9):
            seen = set()

            for j in range(9):

                if board[i][j] == ".":
                    continue

                if board[i][j] in seen:
                    return False

                seen.add(board[i][j])

        # -------------------------
        # Check every column
        # -------------------------
        for j in range(9):
            seen = set()

            for i in range(9):

                if board[i][j] == ".":
                    continue

                if board[i][j] in seen:
                    return False

                seen.add(board[i][j])

      

        #now lets go for the 3rd condition
        for row in range(0,9,3):
            for column in range(0,9,3):
                seen2=set()

                for i in range(row,row+3):
                    for j in range(column,column+3):
                        if board[i][j] in seen2:
                            return False
                        elif board[i][j]==".":
                            continue
                        else:
                            seen2.add(board[i][j])
        
        return True


