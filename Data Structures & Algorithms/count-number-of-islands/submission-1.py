class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == "1" and self.bfs(grid, r, c, visited):
                    count += 1
        return count
    
    def bfs(self, grid, r, c, visited):
        pos = (r,c)
        
        visited.add(pos)
        delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        queue = deque([pos])
        while queue:
            c_r, c_c = queue.popleft()
            for d_r, d_c in delta:
                n_r, n_c = d_r + c_r, d_c + c_c
                row_in = 0 <= n_r < len(grid)
                col_in = 0 <= n_c < len(grid[0])
                n_pos = (n_r, n_c)
                if row_in and col_in and n_pos not in visited and grid[n_r][n_c] == "1":
                    queue.append(n_pos)
                    visited.add(n_pos)
        return True 







