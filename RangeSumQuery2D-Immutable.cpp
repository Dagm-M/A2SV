class NumMatrix {
public:
    vector<vector<int>> M;
    vector<int> prefixSum;
    int m;
    NumMatrix(vector<vector<int>>& matrix) {
        M = matrix;
        int n = M.size();
        m = M[0].size();
        for(int i = 0 ; i < n ; i++)
        {
            prefixSum.push_back(M[i][0]);
                
            for(int j = 1 ; j < m ; j++)
                prefixSum.push_back(prefixSum.back() + M[i][j]);
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        
        
        
        if(row1 == row2 && col1 == col2)
            return M[row1][col1];
        

        int a = 0;
        int b = (prefixSum[row2 * m + col2]) - ((col1 != 0)?prefixSum[row2 * m + col1 - 1]:0);
        while(row1 != row2)
        {
            a += (prefixSum[row1 * m + col2]) - ((col1 != 0)?prefixSum[row1 * m + col1 - 1]:0);
            row1++;
        }
        
    
        
        return a + b;
        
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */
