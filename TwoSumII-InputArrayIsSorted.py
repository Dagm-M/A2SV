class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # left = 0
        # right = len(numbers) - 1

        # while left < right:
        #     if numbers[left] + numbers[right] > target:
        #         right -= 1
        #     elif numbers[left] + numbers[right] < target:
        #         left += 1
        #     else:
        #         return[left + 1,right + 1]

        seen = {}

        for ind,num in enumerate(numbers):
            num2 = (target - num)
            
            if num2 in seen:
                return [seen[num2] + 1, ind + 1]
            else:
                seen[num] = ind
