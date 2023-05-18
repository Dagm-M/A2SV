class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        adjecent = defaultdict(list)

        for edge in edges:
            adjecent[edge[0]].append(edge[1])
            adjecent[edge[1]].append(edge[0])

        def DFS(vertex, visited):
            if vertex == destination:
                return True

            visited.add(vertex)

            for n in adjecent[vertex]:
                if n not in visited:
                    found = DFS(n,visited)

                    if found:
                        return True

            return False

        return DFS(source, set())