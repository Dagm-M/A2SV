class Solution:
    def compare(self,num1,num2):
        if num1 < 10 and num2 < 10:
            return num1 > num2
        first = int(str(num1) + str(num2))
        second = int(str(num2) + str(num1))

        return first > second

    def mergeSort(self,arr):
        if len(arr) > 1:
    
            # Finding the mid of the array
            mid = len(arr)//2
    
            # Dividing the array elements
            L = arr[:mid]
    
            # into 2 halves
            R = arr[mid:]
    
            # Sorting the first half
            self.mergeSort(L)
    
            # Sorting the second half
            self.mergeSort(R)
    
            i = j = k = 0
    
            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if self.compare(L[i],R[j]):
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
    
            # Checking if any element was left
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
    
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1




    def largestNumber(self, nums: List[int]) -> str:

        self.mergeSort(nums)

        nums = list(map(str,nums))

        if nums[0] == "0" and nums[-1] == "0":
            return "0"

        return "".join(nums)
