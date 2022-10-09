class Solution {
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        int n = trips.size();
        vector<int> v(1001,0);
        for(int i = 0; i<n ; i++)
        {
            v[trips[i][2]] += trips[i][0];
            v[trips[i][1]] -= trips[i][0];
        }
        
        for(int i = v.size() -2 ; i >= 0; i--)
        {
            v[i] += v[i+1];
            if(v[i] > capacity)
                return false;
        }
        
        
        return true;
    }
};
