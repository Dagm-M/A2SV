class Solution {
public:
    static bool cmp(vector<string> a , vector<string> b)
    {
        int c = stoi(a[0]), d = stoi(b[0]);

        if(c == d)
            return a[1] > b[1];
        
        return c < d;

    }
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> map;
        int n = words.size();
        vector<vector<string>> v;
        vector<string> vec;
        
        for(int i = 0 ;i < n ; i++)
            map[words[i]]++;
        
        for (auto x : map)
            v.push_back({to_string(x.second), x.first});
        
        make_heap(v.begin(),v.end(),cmp);
        sort_heap(v.begin(),v.end(),cmp);
        
        
        while(k != 0)
        {
            n = v.size();
            vec.push_back(v[n-1][1]);
            v.pop_back();
            k--;
        }

        
        return vec;
    }
};
