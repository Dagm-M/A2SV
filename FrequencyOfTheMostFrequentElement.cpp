class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end(),greater());
        int n = nums.size();
        int j = 0;
        int total = 0;
        
        for(int i = 0 ; i < n ; i++)
        {
            if(nums[i] < nums[j])
            {
                if(k - (nums[j] - nums[i]) >= 0)
                    k -= (nums[j] - nums[i]);
                else
                {
                    k += ((nums[j] - nums[j+1]) * (i - j - 1));
                    j++;
                    i--; 
                }
            }
            
            total = max(total, (i - j + 1));
        }
        
        return total;
    }
};
