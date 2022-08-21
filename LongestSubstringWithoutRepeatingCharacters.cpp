class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int a = 0, b = 0;
        int n = s.size();
        vector<char>v;
        vector<int> vi;
        int sum = 0;
        
        for(int i = 0 ; i < n ; i++)
        {
            int vs = v.size();
            for(int j = 0 ; j < vs ; j++)
            {
                if(s[i] == v[j])
                {
                    a = vi[j] + 1;
                    v.erase(v.begin(),v.begin() +j+1);
                    vi.erase(vi.begin(),vi.begin() +j+1);
  
                    break;
                }
            }
            
            v.push_back(s[i]);
            vi.push_back(i);
            sum = max(sum,b-a+1);
            b++;
        }
        
        return sum;
    }
};
