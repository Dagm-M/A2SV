class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int n = matrix.size();
        int a,b;
        int m = n*n;
        vector<int> linear;
        for(int i = 0 ; i<m ; i++)
        {
            a = i/n;
            b = i%n;
            linear.push_back(matrix[a][b]);
        }
        make_heap(linear.begin(),linear.end(),greater());
        for(int i = 1 ; i<k ; i ++)
        {
            pop_heap(linear.begin(),linear.end(),greater());
            linear.pop_back();
        }
        return linear[0];
    }
};
