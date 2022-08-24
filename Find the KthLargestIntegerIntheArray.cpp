class Solution {
public:
    string kthLargestNumber(vector<string>& nums, int k) {
        sort(nums.begin(), nums.end(), cmp);
        return nums[nums.size() - k];
    }
    
private:
   static bool cmp(string a , string b)
    {
        if(a.size() < b.size())
            return true;
        else if(a.size() == b.size())
            return a<b;
        else
            return false;
    }
};
