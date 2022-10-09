class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int n = p.size();
        int m = s.size();
        int counter = n;
        unordered_map<char,int> pvalue;
        vector<int> v;
        int left = 0, right = 0;
        
        if(n > m)
            return v;
        
        for(int i = 0; i<n; i++)
            pvalue[p[i]] ++;
        
        while(right < m)
        {
            if(pvalue[s[right]] >=  1)
                counter--;
            
            pvalue[s[right]]--;
            
            
            if(counter == 0)
                v.push_back(left);
            

            if((right - left) + 1 == n)
            {
                if(pvalue[s[left]] >= 0)
                    counter++;
                pvalue[s[left]]++;
                left++;
            }
            right++;

        }
        
        
        return v;
        
    }
};
