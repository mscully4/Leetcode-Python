class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        grids = defaultdict(set)
        columns = defaultdict(set)
        
        for r in range(len(board)):
            used = set()
            for c in range(len(board[r])):
                if board[r][c] != '.':
                    if board[r][c] in used:
                        return False

                    if board[r][c] in columns[c]:
                        return False

                    node = grids[(3 * (r // 3)) + (c // 3)]
                    if board[r][c] in node:
                        return False

                    used.add(board[r][c])
                    columns[c].add(board[r][c])
                    node.add(board[r][c])
        
        return True
                