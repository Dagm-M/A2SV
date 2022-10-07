class Solution {
public:
    vector<int> partitionLabels(string s) {
        int n = s.size();
        int left = 0;
        int right = n-1;
        int temp;
        int temp2;
        vector<int> v;
        if(n == 1)
        {
            v.push_back(1);
            return v;
        }
        
        while(left < n)
        {
            if(s[left] == s[right])
            {
                temp2 = left;
                left++;
                temp = n - 1;
                while(left <= right)
                {
                    if(temp <= right)
                    {
                        left++;
                        temp = n;
                    }
                    else if(s[left] == s[temp])
                    {
                        left++;
                        right = temp;
                        temp = n;
                    }
                    temp--;
                }
                v.push_back(right - temp2 + 1);
                right = n;
            }
            else if(left == right)
            {
                v.push_back(1);
                left++;
                right = n;
            }
            right--;
        }
        
        return v;
    }
};
