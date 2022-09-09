class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char, int> m;
        vector<vector<int>> v;
        int a;
        int counter = 0;
        int s = tasks.size();
        int total = 0;
        
        if(n == 0)
            return s;
        
        for(int i = 0 ; i < s ; i++)
            m[tasks[i]]++;
        
        for(auto x: m)
            v.push_back({x.second, x.first});
        
        sort(v.begin(),v.end(),greater());
        vector<vector<int>>temp;
        while(!m.empty())
        {
            counter = 0;
            a = n + 1;
            int b = v.size();
        
            for(int i = 0 ; i < b ;i++)
            {
                if(m.find(v[i][1]) == m.end())
                    continue;
                if(a == 0)
                {
                    counter = 0;
                    i = 0;
                    a = n + 1;
                    sort(v.begin(),v.end(),greater());
                }
                v[i][0]--;
                if(v[i][0] == 0)
                    m.erase(v[i][1]);
                
                counter++;
                total++;
                a--;
            }
            

            total += (n - (counter - 1));
            
        }
            

        return total - (n - (counter - 1));
    }
};
