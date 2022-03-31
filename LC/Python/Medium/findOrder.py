class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        sorted_graph = []
        in_degree = {i: 0 for i in range(numCourses)}
        graph =  defaultdict(list)
        
        for child, parent in prerequisites:
            in_degree[child] += 1
            graph[parent].append(child)
            
        sources = deque([k for k in in_degree if in_degree[k]==0])
        
        while sources:
            vertex = sources.popleft()
            sorted_graph.append(vertex)
            
            for child in graph[vertex]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    sources.append(child)
                    
        if len(sorted_graph)!=numCourses:
            return []
        
        return sorted_graph