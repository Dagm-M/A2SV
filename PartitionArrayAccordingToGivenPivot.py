class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lessThan = []
        equalTo = []
        greaterThan = []

        for num in nums:
            if num < pivot:
                lessThan.append(num)
            elif num > pivot:
                greaterThan.append(num)
            else:
                equalTo.append(num)

        return lessThan + equalTo + greaterThan
