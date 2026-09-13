class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # loop through each 3 x 3 section (2d loop)
        # add each number in rows, columns, and squares to a separate hashmap
            # if set.add() == false:
                # return false
        # return true

        # rows
        for r in range(9):
            seen = set()
            for c in range(9):
                v = board[r][c]
                if v == '.': 
                    continue
                if v in seen:
                    return False
                seen.add(v)

        # cols
        for c in range(9):
            seen = set()
            for r in range(9):
                v = board[r][c]
                if v == '.': 
                    continue
                if v in seen:
                    return False
                seen.add(v)

        # squares (hardcoded coords)
        squares = [
            [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)],
            [(0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)],
            [(0,6),(0,7),(0,8),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8)],
            [(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1),(5,2)],
            [(3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3),(5,4),(5,5)],
            [(3,6),(3,7),(3,8),(4,6),(4,7),(4,8),(5,6),(5,7),(5,8)],
            [(6,0),(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2)],
            [(6,3),(6,4),(6,5),(7,3),(7,4),(7,5),(8,3),(8,4),(8,5)],
            [(6,6),(6,7),(6,8),(7,6),(7,7),(7,8),(8,6),(8,7),(8,8)],
        ]

        for sq in squares:
            seen = set()
            for r, c in sq:
                v = board[r][c] # accessing board coordinates
                if v == '.': 
                    continue
                if v in seen:
                    return False
                seen.add(v)
        return True
        