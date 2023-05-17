from typing import List


from typing import List

from collections import defaultdict, deque


class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        depend = defaultdict(int)
        adj = defaultdict(list)
        ans = [0] * n
        seen = set()
        time = 1
        
        
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
            depend[edge[1]] += 1
        
        q = deque()
        
        for val in range(1, n + 1):
            if depend[val] == 0:
                q.append(val)
                ans[val-1] = str(time)
        count = 0
        while q:
            if count == 0:
                time += 1
                count = len(q)
            val = q.popleft()
            count -= 1
            
            
            seen.add(val)
            
            for ad in adj[val]:
                depend[ad] -= 1
                if ad not in seen and depend[ad] < 1:
                    q.append(ad)
                    ans[ad - 1] = str(time)
                    seen.add(ad)
        
        return " ".join(ans)
