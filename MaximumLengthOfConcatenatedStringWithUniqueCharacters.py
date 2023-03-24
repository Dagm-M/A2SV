class Solution:
    def maxLength(self, arr: List[str]) -> int:
        maxlen = 0
        seen = defaultdict(int)

        def length(curr,state):
            nonlocal maxlen
            if curr >= len(arr):
                return

            for i in range(curr,len(arr)):
                for c in arr[i]:
                    seen[c] += 1
                state.append(arr[i])

                n = len(seen)
                if n == len("".join(state)):
                    maxlen = max(maxlen, n)
                    length(i+1,state)

                state.pop()
                for c in arr[i]:
                    seen[c] -= 1
                    if seen[c] == 0:
                        del seen[c]
                    
        
        length(0,[])

        return maxlen
