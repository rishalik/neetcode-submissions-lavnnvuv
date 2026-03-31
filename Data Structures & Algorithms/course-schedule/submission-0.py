class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        visiting = set()
        graph = self.design_graph(numCourses, prerequisites)
        for node in graph:
            if self.explore(graph, node, visited, visiting):
                return False
        return True
    

    def explore(self, graph, node, visited, visiting):
        if node in visited:
            return False
        
        if node in visiting:
            return True
        
        visiting.add(node)
        for ne in graph[node]:
            if self.explore(graph, ne, visited, visiting):
                return True
        
        visiting.remove(node)
        visited.add(node)
        return False


    def design_graph(self, numCourses, prerequisites):
        graph = {}

        for n in range(numCourses):
            graph[n] = []
        
        for edge in prerequisites:
            a, b = edge
            graph[a].append(b)
        return graph