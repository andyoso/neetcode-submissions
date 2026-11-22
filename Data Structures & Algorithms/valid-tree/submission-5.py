class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        hash_map = {i:[] for i in range(n)}
        for n1, n2 in edges:
            hash_map[n1].append(n2)
            hash_map[n2].append(n1)
        visited = set()
        def dfs(node, pre):
            if node in visited:
                return False
            visited.add(node)
            for n in hash_map[node]:
                if pre == n:
                    continue
                if not dfs(n, node):
                    return False
            return True
        return dfs(0, -1) and len(visited) == n
