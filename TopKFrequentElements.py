class Solution:
    def quickSort(self, nums, left, right):
        if left >= right:
            return
        
        if right - left == 1:
            if nums[right][0] < nums[left][0]:
                nums[right], nums[left] = nums[left], nums[right]
            return 

        arr = [[nums[left][0],left], [nums[left + (right - left)//2][0], left + (right - left)//2], [nums[right][0], right]]
        maximum = max(arr)
        minimum = min(arr)
        for a in arr:
            if a != maximum and a != minimum:
                pivot = a[1]
                break
        
        nums[left],nums[pivot] = nums[pivot],nums[left]

        pivot = left
        read = pivot + 2
        write = pivot + 1

        while read <= right:
            while write < read and nums[pivot][0] >= nums[read][0]:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1
            read += 1

        if nums[pivot][0] > nums[write][0]:
            nums[pivot], nums[write] = nums[write], nums[pivot]
            pivot = write
        else:
            nums[pivot], nums[write-1] = nums[write-1], nums[pivot]
            pivot = write -1


        self.quickSort(nums,pivot+1,right)

        self.quickSort(nums,left,pivot-1)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        newNums = []
        ans = []
        
        for key,value in freq.items():
            newNums.append([value,key])

        self.quickSort(newNums,0,len(newNums)-1)
        n = len(newNums) - 1

        for i in range(n, n - k, -1):
            ans.append(newNums[i][1])

        return ans
