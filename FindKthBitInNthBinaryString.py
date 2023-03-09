class Solution:
    def operation(self,arr):
        newArr = arr.copy()
        newArr.append(1)
        for i in range(len(arr)):
            arr[i] = (1-arr[i])
        
        arr.reverse()
        newArr.extend(arr)
        return newArr

    def find(self,k,arr):
        if k <= len(arr):
            return arr[k-1]

        n = len(arr)
        newArr = self.operation(arr)
        return self.find(k,newArr)

    def findKthBit(self, n: int, k: int) -> str:
        return str(self.find(k,[0]))
