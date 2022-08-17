class Solution {
public:
    int compress(vector<char>& chars) {
        int n = chars.size();
        int sum = 1;
        char c = chars[0];
        vector<char> v;
        v.push_back(c);
        string s;
        
        for(int i = 1 ; i<n ; i++)
        {
            if(c == chars[i])
                sum++;
            else
            {
                if(sum != 1)
                {
                    s = to_string(sum);
                    for(int j = 0; j< s.size() ; j++)
                        v.push_back(s[j]);
                    v.push_back(chars[i]);
                    sum = 1;
                }
                else
                    v.push_back(chars[i]);
                c = chars[i];
                
            }
            
        }
        
        s = to_string(sum);
        if(sum != 1)
        {
            for(int j = 0; j< s.size() ; j++)
                        v.push_back(s[j]);
        }
        
        
        chars = v;
        return v.size();
    }
};
