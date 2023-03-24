class Solution:
    def quickSort(self, nums, left, right,k):
        if left >= right:
            return nums[left]
        
        if right - left == 1:
            if nums[right] < nums[left]:
                nums[right], nums[left] = nums[left], nums[right]
            return nums[len(nums) - k]

        arr = [[nums[left],left], [nums[left + (right - left)//2], left + (right - left)//2], [nums[right], right]]
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
            while write < read and nums[pivot] >= nums[read]:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1
            read += 1

        if nums[pivot] > nums[write]:
            nums[pivot], nums[write] = nums[write], nums[pivot]
            pivot = write
        else:
            nums[pivot], nums[write-1] = nums[write-1], nums[pivot]
            pivot = write -1

        if k == len(nums) - pivot:
            return nums[pivot]
        elif len(nums) - k >pivot:
            return self.quickSort(nums,pivot+1,right,k)

        return self.quickSort(nums,left,pivot-1,k)


    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSort(nums,0,len(nums)-1, k)

            
