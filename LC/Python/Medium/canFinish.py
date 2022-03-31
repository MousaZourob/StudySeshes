class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        sorted_graph = []
        
        in_degree = {i: 0 for i in range(numCourses)}
        graph =  defaultdict(list)
        
        for parent, child in prerequisites:
            graph[parent].append(child)
            in_degree[child] += 1
        
        sources = deque()
        for key in in_degree:
            if in_degree[key] == 0:
                sources.append(key)
        
        while sources:
            vertex = sources.popleft()
            sorted_graph.append(vertex)
            for child in graph[vertex]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    sources.append(child)
        
        return len(sorted_graph) == numCourses
    