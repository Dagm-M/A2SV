class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        int n = nums.size();
        int temp;
        sort(nums.begin(), nums.end());
        
        for(int i = 0; i<n-1 ; i+=2)
        {
            if(nums[i] < nums[i + 1])
            {
                temp = nums[i];
                nums[i] = nums[i + 1];
                nums[i + 1] = temp;
            }

        }
        
        return nums;
    }
};
