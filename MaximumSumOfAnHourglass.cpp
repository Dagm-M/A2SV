class Solution {
public:
    int maxSum(vector<vector<int>>& grid) {
        vector<vector<int>> gridSum(grid.size());
        vector<vector<int>> maxGrid(grid.size());
        for(int i = 0; i < grid.size(); i++)
        {
            gridSum[i].push_back(grid[i][0]);
            for(int j = 1; j < grid[i].size(); j++)
            {
                gridSum[i].push_back(grid[i][j] + gridSum[i][j-1]);
                if(j == 2)
                    maxGrid[i].push_back(gridSum[i][j]);
                else if(j > 2)
                    maxGrid[i].push_back(gridSum[i][j] - gridSum[i][j - 3]);
            }
        }
 
        int maxNum = 0;

        for(int i = 0; i < maxGrid.size() - 2; i++)
        {
            for(int j = 0; j < maxGrid[i].size(); j++)
                maxNum = max(maxNum, maxGrid[i][j] + maxGrid[i+2][j] + grid[i+1][j+1]);
        }


        return maxNum;
    }
};
