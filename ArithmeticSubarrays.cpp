class Solution {
public:
    vector<bool> checkArithmeticSubarrays(vector<int>& nums, vector<int>& l, vector<int>& r) {
        vector<bool> answer;
        vector<int> temp;
        int  n = l.size();
        int d;
        int m;
        bool A;
        for(int i = 0 ; i < n; i++)
        {
            temp.assign(nums.begin() + l[i], nums.begin() + r[i] + 1);
            sort(temp.begin(),temp.end());
            d = temp[1] - temp[0];
            m = temp.size();
            A = true;
            for(int i = 1 ; i < m-1 ; i++)
            {
                if(d != temp[i+1] - temp[i])
                {
                    A = false;
                    break;
                }
            }
            answer.push_back(A);
        }
        
        return answer;
    }
};
