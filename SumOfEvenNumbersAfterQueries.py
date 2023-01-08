class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = 0
        numOfEven = []

        for num in nums:
            if num % 2 == 0:
                evenSum += num

        for val,index in queries:
            if nums[index] % 2 == 0:
                if (nums[index] + val) % 2 == 0:
                    evenSum += val
                else:
                    evenSum -= nums[index]
                
                nums[index] += val
                    
            else:
                if (nums[index] + val) % 2 == 0:
                    nums[index] += val
                    evenSum += nums[index]
                else:
                    nums[index] += val

            numOfEven.append(evenSum)


        return numOfEven
