from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        hash_map = {i:[] for i in range(n)}
        for n1, n2 in edges:
            hash_map[n1].append(n2)
            hash_map[n2].append(n1)
        visited = set()
        queue = deque([[0, -1]])
        visited.add(0)
        while queue:
            node, pre_node = queue.popleft()
            for nei  in hash_map[node]:
                if nei == pre_node:
                    continue
                if nei in visited:
                    return False
                queue.append([nei, node])
                visited.add(nei)
        return len(visited) == n
        # TC :　O(n + e), where n is the number of nodes and e is number of edges
        # SC :  O(n + e)