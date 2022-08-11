class Solution {
public:
    int minPairSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int size = nums.size();
        int n = size - 1;
        int m = 0;
        int num;
        int max = 0;
        for(int i = 0 ; i < size/2 ; i++)
        {
            num = (nums[n] + nums[m]);
            
            if(num > max)
                max = num;
            n--;
            m++;
        }
        return max;
    }
};
