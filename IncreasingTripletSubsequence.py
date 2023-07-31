class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        beforeCurrent = inf
        current = inf
        counter = 0

        for num in nums:
            if beforeCurrent >= num:
                beforeCurrent = num
            elif current >= num:
                current = num
            else:
                return True

        return False
