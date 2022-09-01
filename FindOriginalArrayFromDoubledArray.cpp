class Solution {
public:
    vector<int> findOriginalArray(vector<int>& changed) {
        sort(changed.begin(), changed.end());
        queue<int> q;
        vector<int>v;
        int n = changed.size();

        
        for(int i = 0 ; i<n ; i++)
        {
           if(!q.empty() && q.front() == changed[i]) 
               q.pop();
            else
            {
                v.push_back(changed[i]);
                q.push(changed[i]*2);
            }
        }
        
        int s = v.size();
        if(s > n/2)
            return {};
        
        return v;
        
    }
};
