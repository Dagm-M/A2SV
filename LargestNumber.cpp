class Solution {
private:
    static bool cmp(int a , int b)
    {
        if(a < 10 && b < 10)
            return a > b;
        string x = to_string(a);
        string y = to_string(b);
        string z = x + y;
        y = y + x;
        int n = z.size();
        for(int i = 0 ; i < n; i++)
        {
            if((z[i] - '0') > (y[i] - '0'))
                return true;
            else if((z[i] - '0') < (y[i] - '0'))
                return false;
        }
        return true;
    }
public:
    string largestNumber(vector<int>& nums) {
        int n =nums.size();
        string s;

            
        sort(nums.begin(),nums.end(),cmp);

        for(int i = 0 ; i < n ; i++)
        {
            if(!s.empty() || nums[i] != 0)
                s = s + to_string(nums[i]);
        }
        if(s.empty())
            s = '0';

        return s;
        
    }
};
