class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sum = 0
        remender = defaultdict(int)
        count = 0

        for num in nums:
            sum += num

            if sum % k in remender:
                count += remender[sum % k]
            
            remender[sum % k] += 1

            if sum % k == 0:
                count += 1

        return count
