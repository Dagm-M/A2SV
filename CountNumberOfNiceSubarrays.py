class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        right = 0
        evenAfterK = 0
        count = 0
        nice = 0
        nums.append(0)

        for right in range(n+1):

            if nums[right] % 2 != 0:
                count += 1

            while (count == k and right == n) or count > k:
                nice += evenAfterK
                if nums[left] % 2 != 0:
                    count -= 1
                left += 1
                if not ((count == k and right == n) or count > k):
                    evenAfterK = 0

            
            if count == k:
                evenAfterK += 1


        return nice
