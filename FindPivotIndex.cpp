class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        vector<int>prefixSum;
        prefixSum.push_back(nums[0]);
        int n = nums.size();
        for(int i = 1 ; i<n ; i++)
        {
             prefixSum.push_back(prefixSum[i-1] + nums[i]);
        }
        
        if(prefixSum[n-1] - prefixSum[0] == 0)
            return 0;
        
        for(int i = 1 ; i<n ; i++)
        {
            if(prefixSum[n-1] - prefixSum[i] == prefixSum[i-1])
                return i;
        }
        return -1;
    }
};
