class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for char in s:
            if len(stack):
                if char == stack[-1][0]:
                    stack[-1][1] += 1
                else:
                    stack.append([char,1])
                
                if stack[-1][1] == k:
                    stack.pop()

            else:
                stack.append([char,1])

        ans = []
        for chr,i in stack:
            ans.append(chr * i)

        return "".join(ans)
