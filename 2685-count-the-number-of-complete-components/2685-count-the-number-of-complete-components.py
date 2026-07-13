class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        ans = 0

        def dfs(node):

            visited.add(node)
            component.append(node)

            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)

        for i in range(n):

            if i not in visited:

                component = []

                dfs(i)

                nodes = len(component)

                edge_count = 0

                for node in component:
                    edge_count += len(graph[node])

                edge_count //= 2

                if edge_count == nodes * (nodes - 1) // 2:
                    ans += 1

        return ans