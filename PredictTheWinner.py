class Solution:
    def calculate(self,nums,l,r,scoreP1,scoreP2,turn):
        if l >= r:
            if l == r:
                if turn == 1:
                    scoreP1 += nums[l]
                else:
                    scoreP2 += nums[l]

            return scoreP1 >= scoreP2
        
        if turn == 1:
            value1 = self.calculate(nums,l+1,r,scoreP1+nums[l],scoreP2,2)
            if value1 != True:
                value2 = self.calculate(nums,l,r-1,scoreP1+nums[r],scoreP2,2)

            return value1 or  value2

        else:
            value1 = self.calculate(nums,l+1,r,scoreP1,scoreP2+nums[l],1)
            if value1 != False:
                value2 = self.calculate(nums,l,r-1,scoreP1,scoreP2+nums[r],1)

            return value1 and value2

    def PredictTheWinner(self, nums: List[int]) -> bool:
        l = 0
        r = len(nums) - 1
        scoreP1 = 0
        scoreP2 = 0

        return self.calculate(nums,l,r,scoreP1,scoreP2,1)
