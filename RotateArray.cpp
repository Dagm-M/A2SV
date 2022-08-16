class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        if(n == k)
            return;//do noting
        else if(k == 0)
            return;//do nothing
        else if(n == 1)
            return;//do nothing
        else
        {
            while(n-k < 0)
                k = k%n;
            vector<int> v(nums.begin() ,nums.end() - k);

            v.insert(v.begin(), nums.end() - k, nums.end());
            nums = v;
        }
    }
};
