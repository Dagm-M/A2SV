class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        int n = points.size();
    vector<vector<double>> result(n,vector<double>(2,0));

    for (int i = 0; i < n; i++)
    {
        result[i][0]=(pow((pow(points[i][0], 2) + pow(points[i][1], 2)), 0.5));
        result[i][1]=i;
        
    }
    vector<vector<int>> closest(k,vector<int>(2,0));
    
    sort(result.begin(),result.end());
        for(int i=0; i<k ; i++)
        {
            closest[i] = points[result[i][1]];
        }
        
        return closest;
    }
};
