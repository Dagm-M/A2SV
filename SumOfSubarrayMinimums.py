class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        val = []
        total = 0
        mod = pow(10,9) + 7

        for i in range(len(arr)):

            while len(stack) != 0 and arr[stack[-1]] > arr[i]:
                stack.pop()

            if len(stack) == 0:
                val.append((i+1) * arr[i])
            else:
                val.append(val[stack[-1]] + (i - stack[-1]) * arr[i])

            total += val[-1]
            stack.append(i)
            total %= mod

        return total
