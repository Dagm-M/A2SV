class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // vector<int> answer;
        int n = nums.size();
        int product = 1;
        int Zero = 0;
        for(int i = 0 ; i<n ; i++)
        {
            if(nums[i] != 0)
                product *= nums[i];
            else
                Zero ++;
        }
        
        
        for(int i = 0 ; i<n ; i++)
        {
            if(nums[i] != 0)
            {
                if(Zero > 0)
                    nums[i] = 0;
                else
                    nums[i] = product/nums[i];
            }
            else
            {
                if(Zero > 1)
                    nums[i] = 0;
                else
                    nums[i] = product;
            }
        }
    
        return nums;
    }
};
