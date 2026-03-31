class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                size = self.bfs(grid, r, c, visited)
                if size > max_area:
                    max_area = size 
        return max_area
    
    def bfs(self, grid, r, c, visited):
        pos = (r,c)
        if pos in visited or grid[r][c] == 0:
            return 0
        visited.add(pos)
        queue = deque([pos])
        delta = [(1,0), (0,1), (0,-1), (-1,0)]
        size = 0
        while queue:
            size += 1
            c_r, c_c = queue.popleft()
            for each in delta:
                d_r, d_c = each
                n_r, n_c = d_r + c_r, d_c + c_c
                row_in = 0 <= n_r < len(grid)
                col_in = 0 <= n_c < len(grid[0])
                n_pos = (n_r, n_c)
                if row_in and col_in and n_pos not in visited and grid[n_r][n_c] != 0:                    
                    queue.append(n_pos)
                    visited.add(n_pos)
        return size


