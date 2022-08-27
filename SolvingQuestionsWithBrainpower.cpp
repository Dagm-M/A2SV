class Solution {
public:
    long long mostPoints(vector<vector<int>>& questions) {
        
        int n = questions.size();
        vector<long long> M(n,0);
        
        for(int i = n-1 ; i >= 0 ; i--)
        {
            if(i + questions[i][1] + 1 < n)
                M[i] = max(questions[i][0] + M[i + questions[i][1] + 1], M[i + 1]);
                
            else if(i +1 < n)
                M[i] = max((long long)questions[i][0], M[i + 1]);
    
            else
                M[i] = questions[i][0];
        }
        
        return M[0];
    }
};
