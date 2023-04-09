class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = set()
        seen = set()

        for edge in edges:
            if edge[0] not in seen:
                ans.add(edge[0])
            
            ans.discard(edge[1])

            seen.add(edge[0])
            seen.add(edge[1])

        
        return list(ans)
