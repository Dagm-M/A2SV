class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(),intervals.end());
        int n = intervals.size();
        vector<vector<int>>v;
        int a = 1;
 
        if(n == 1)
            return intervals;
        for(int i = 0 ; a < n  ; )
        {
            if(intervals[i][0] <= intervals[a][0] && intervals[a][0] <= intervals[i][1])
            {
                intervals[i][1] = max(intervals[i][1],intervals[a][1]);

                a++;
                if(a == n)
                    v.push_back({intervals[i][0],intervals[i][1]});
            }
            else
            {
                v.push_back({intervals[i][0],intervals[i][1]});
                i = a;
                a++;
                if(a == n)
                    v.push_back({intervals[i][0],intervals[i][1]});

        
            }
        }
        return v;
    }
};
