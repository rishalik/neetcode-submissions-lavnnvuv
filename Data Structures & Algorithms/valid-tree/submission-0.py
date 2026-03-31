class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        visited = set()
        graph = self.design_graph(n, edges)
        if self.has_cycle(graph, 0, -1, visited):
            return False
        
        return len(visited) == n
    
    def has_cycle(self, graph, node, parent, visited):
        if node in visited:
            return True
        
        visited.add(node)

        for ne in graph[node]:
            if ne == parent:
                continue
            if self.has_cycle(graph, ne, node, visited):
                return True

        return False

    def design_graph(self, n, edges):
        graph = {}
        for i in range(n):
            graph[i] = []
        
        for edge in edges:
            a,b = edge
            graph[a].append(b)
            graph[b].append(a)
        return graph