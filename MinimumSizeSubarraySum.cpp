class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int n = nums.size();
        int subarray = n;
        for(int i = 0 ; i<n ; i++)
        {
            if(i > 0)
                nums[i] += nums[i-1];
            if(nums[i] >= target)
                subarray = min(subarray,i+1);
        }
        
        int left = 0, right = 1;
        
        if(nums[n-1] < target)
            return 0;
        
        if(n == 1)
            return 1;
        
        while(left < right)
        {
            if(nums[right] - nums[left] >= target)
            {
                subarray = min(subarray, right-left);
                
                left++;     
            }
            
            else
            {
                if(right == n-1)
                    break;
                else
                    right++;
            }
        }
        
            
        
        return subarray;
    }
};
