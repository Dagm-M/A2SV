class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxelement = arr[-1]
        arr[-1] = -1

        for index in range(len(arr)-2, -1, -1):
            temp = arr[index]
            arr[index] = maxelement
            maxelement = max(maxelement,temp)

        return arr
