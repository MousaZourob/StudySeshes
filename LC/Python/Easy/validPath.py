class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        neighbours = defaultdict(list)
        for n1, n2 in edges:
            neighbours[n1].append(n2)
            neighbours[n2].append(n1)
        
        def dfs(node, end, seen):
            if node == end:
                return True
            if node in seen:
                return False
            
            seen.add(node)
            for n in neighbours[node]:
                if dfs(n, end, seen):
                    return True
            
        seen = set()    
        return dfs(start, end, seen)