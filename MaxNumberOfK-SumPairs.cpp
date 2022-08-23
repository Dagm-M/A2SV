class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end());
        int n = nums.size();
        int total = 0;
        int a =0 , b = n-1;
        while(a < b)
        {
            if(nums[a] + nums[b] == k)
            {
                total++;
                a++;
                b--;
            }
            else if(nums[a] + nums[b] > k)
                b--;
            else
                a++;
        }
        
        return total;
    }
};
