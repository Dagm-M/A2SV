class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        int n = cardPoints.size();
        int sum = 0;
        int maxs = 0;
        int right = n - k, left = right;
        
        while(left < n)
        {
            if(k <= 0)
            {
                sum -= cardPoints[left];
                left++; 
            }
            
            sum += cardPoints[right];
            right++;
            k--;
            maxs = max(sum, maxs);
            if(right >= n)
                right = 0;
            
        }
        
        return maxs;
    }
};
