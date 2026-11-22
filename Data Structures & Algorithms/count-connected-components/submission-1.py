class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hash_map = {i:[] for i in range(n)}
        for n1, n2 in edges:
            hash_map[n1].append(n2)
            hash_map[n2].append(n1)
        visited = set()
        output = 0
        def dfs(node, pre):
            if node in visited:
                return
            visited.add(node)
            for nei in hash_map[node]:
                if nei == pre:
                    continue
                if nei not in visited:
                    dfs(nei, node)         
        for j in range(n):
            if j not in visited:
                output += 1
                dfs(j, -1)
        return output
        # TC : O(n + e), where n is number of nodes and e is the number of edges
        # SC : O(n + e)