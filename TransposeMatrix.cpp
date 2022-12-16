class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {
        int n = matrix.size();
        vector<vector<int>> transpose(matrix[0].size());
        for(int i = 0; i < n; i++)
            for(int j = 0; j < matrix[i].size(); j++)
                transpose[j].push_back(matrix[i][j]);

        return transpose;
    }
};
