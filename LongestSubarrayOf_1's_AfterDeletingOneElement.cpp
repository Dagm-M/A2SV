class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int n = nums.size();
        int left = 0 , right = 0;
        int deleted = -1;
        int sum = 0;
        int maxsum = 0;
        
        while(right < n)
        {
            if(nums[right] == 0 && deleted >= 0)
            {
                sum -= (deleted - left);
                left = deleted + 1;
                deleted = right;
            }
            
            else if(nums[right] == 0)
                deleted = right;
            else
                sum++;
            
            right++;
            
            maxsum = max(maxsum, sum);
        }
        
        if(deleted < 0)
            maxsum--;
        
        return maxsum;
    }
};
