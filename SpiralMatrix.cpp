class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int m = matrix[0].size();
        int nn;
        int mm;
        int x = 0;
        vector<int>v;
        int total = n * m;
        
        while(total > 0)
        {
            nn = x;
            mm = x;
            while(mm != m)
            {
                v.push_back(matrix[nn][mm]);
                mm++;
                total --;
            }
            
            mm--;
            nn++;
            
            if(total <= 0)
                break;
            
            while(nn != n)
            {
                v.push_back(matrix[nn][mm]);
                nn++;
                total --;
            }
            
            nn--;
            mm--;
            
           if(total <= 0)
                break;
            
            while(mm >= x)
            {
                v.push_back(matrix[nn][mm]);
                mm--;
                total --;
            }
            
            mm++;
            nn--;
            
           if(total <= 0)
                break;
            
            while(nn >= x+1)
            {
                v.push_back(matrix[nn][mm]);
                nn--;
                total--;
            }
            
            
            
            m--;
            n--;
            x++;
            
        }
        return v;
    }
};
