class Solution:
    def numIslands(self, grid):
        islands = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    print(r, c)
                    islands += 1
                    grid[r][c] = "0"
                    self.flip_island(r, c, grid) 
        return islands
                    
    def flip_island(self, r, c, grid):
        left = c - 1
        right = c + 1
        up = r - 1
        down = r + 1
        
        # print(r, c, grid)
        if left >= 0 and grid[r][left] == "1":
            grid[r][left] = "0"
            self.flip_island(r, left, grid)
        
        if right < len(grid[0]) and grid[r][right] == "1":
            grid[r][right] = "0"
            self.flip_island(r, right, grid)
            
        if up >= 0 and grid[up][c] == "1":
            grid[up][c] = "0"
            self.flip_island(up, c, grid)
        
        if down < len(grid) and grid[down][c] == "1":
            grid[down][c] = "0"
            self.flip_island(down, c, grid)