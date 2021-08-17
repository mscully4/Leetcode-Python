class Solution:
    def snakesAndLadders(self, board) -> int:
        new_board = []
        for i, row in enumerate(board[::-1]):
            new_board.extend(row if i % 2 == 0 else row[::-1])
            
        
        depth = 1
        possible_locations = [0]  
        
        while True:
            new_psbl_locs = set()
            for loc in possible_locations:
                for dis in range(1, len(new_board) - loc if loc + 6 >= len(board) ** 2 else 7):
                    new_loc = loc + dis if new_board[loc + dis] == -1 else new_board[loc + dis] - 1
                    if new_loc == len(new_board) - 1:
                        return depth
                    new_psbl_locs.add(new_loc)

            if new_psbl_locs == possible_locations:
                return -1
            
            possible_locations = new_psbl_locs
            depth += 1