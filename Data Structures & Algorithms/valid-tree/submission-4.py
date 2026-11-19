class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree has n-1 edges and no cycles, we need to check cycles
        if len(edges) != n - 1:
            return False
        
        neighbors = {node: [] for node in range(n)}
        for node, edge in edges:
            neighbors[node].append(edge)
            neighbors[edge].append(node)
        
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            
            for neighbor in neighbors[node]:
                if neighbor == parent:
                    continue
                
                if not dfs(neighbor, node):
                    return False
            
            return True
        
        if not dfs(0, -1):
            return False
        
        return len(visited) == n


        