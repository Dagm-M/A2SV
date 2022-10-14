class Solution {
public:
    int maxSumTwo(vector<int>& nums, int firstLen, int secondLen) {
        int firstLeft = 0, firstRight = 0;
        int secondLeft, secondRight;
        int firstSum = 0, secondSum = 0, maxSecond = 0, maxSum = 0;
        
        while(firstRight < nums.size())
        {
            if(firstRight - firstLeft + 1 > firstLen)
            {
                firstSum -= nums[firstLeft];
                firstLeft++;
            }
            
            if(firstRight - firstLeft + 1 == firstLen)
            {
                secondLeft = firstRight + 1;
                secondRight = firstRight + 1;
                secondSum = 0;
                maxSecond = 0;
                while(secondRight < nums.size())
                {
                    if(secondRight - secondLeft + 1 > secondLen)
                    {
                        secondSum -= nums[secondLeft];
                        secondLeft++;
                    }
                    
                    secondSum += nums[secondRight];
                    maxSecond = max(maxSecond, secondSum);
                    secondRight++;
                }
            }
            
            
            firstSum += nums[firstRight];
            maxSum = max(maxSum, firstSum + maxSecond);
            firstRight++;
        }
        
        return maxSum;
        
    }
    
    int maxSumTwoNoOverlap(vector<int>& nums, int firstLen, int secondLen)
    {
        int a = maxSumTwo(nums,firstLen,secondLen);
        int b = maxSumTwo(nums,secondLen, firstLen);
        return max(a,b);
    }
};
