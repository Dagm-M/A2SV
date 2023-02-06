class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        k = k % size

        if k == 0:
            return
        elif k == size:
            return
        elif size == 1:
            return

        nums[size-k: ], nums[: size - k] = nums[:size - k], nums[size - k: ]

