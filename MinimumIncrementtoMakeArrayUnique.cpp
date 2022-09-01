class Solution {
public:
    int minIncrementForUnique(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int minimum = 0;
        int n = nums.size();
        
        for(int i = 0 ; i< n-1 ; i++)
        {
            if(nums[i] >= nums[i+1])
            {
                minimum += nums[i]+1 - nums[i+1];
                nums[i+1] = nums[i] + 1;
            }
        }
        return minimum;
            
    }
};
