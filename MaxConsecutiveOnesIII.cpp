class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int n = nums.size();
        int left = 0;
        int right = 0;
        int max = 0;
        
        while(right != n)
        {
            if(nums[right] == 0)
                k--;
            
            if(k<0)
            {
                if(nums[left] == 0)
                    k++;
                left++;
            }
            
            if(max < right - left + 1)
                max = right - left + 1; 
            
            right++;
        }
        
        return max;

    }
};
