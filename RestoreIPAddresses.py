class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []


        def backTrack(curr,arr):
            if curr >= len(s):
                if len(arr) == 4:
                    ans.append(".".join(arr))
                return


            for i in range(curr,len(s)):
                val = s[curr:i+1]
                num = int(val)

                if num > 255 or (len(val) != 1 and val[0] == "0"):
                    break

                if len(arr) < 4:
                    arr.append(val)
                    backTrack(i+1,arr)
                    arr.pop()
               

        backTrack(0,[])

        return ans
