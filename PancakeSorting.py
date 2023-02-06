class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        n = len(arr)
        i = len(arr) - 1

        while i >= 0:

            if i == 0 and arr[i] == 1:
                break
            
            if arr[i] == n:

                if arr[i] != i+1:
                    if i != 0:
                        temp = arr[0:i+1]
                        temp.reverse()
                        arr = temp + arr[i+1:]
                        flips.append(i+1)

                    temp = arr[0:n]
                    temp.reverse()
                    arr = temp + arr[n:]
                    flips.append(n)

                n -= 1
                i = n - 1

            else:
                i -= 1

        return flips
