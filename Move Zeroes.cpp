class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n = nums.size();
        for(int i = 0, j = n-1 ; i<n; i++,j--)
        {
            if(nums[i] == 0)
            {
                nums.erase(nums.begin() + i);
                nums.push_back(0);
            }
            if(nums[j] == 0)
            {
                nums.erase(nums.begin() + j);
                nums.push_back(0);
            }
        }
    }
};
