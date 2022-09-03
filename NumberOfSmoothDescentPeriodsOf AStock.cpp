class Solution {
public:
    long long getDescentPeriods(vector<int>& prices) {
        int n = prices.size();
        long long subarr = 1;
        long long total = n;
        
        if(n == 1)
            return 1;
        for(int i = 0 ; i<n-1 ;i++)
        {
            if(prices[i] - prices[i+1] == 1)
                subarr++;
            else
            {
                total += (subarr * (subarr + 1))/2 - subarr;
                subarr = 1;
            }
        }
        
        if(prices[n-2] - prices[n-1] == 1)
        {
            total += (subarr * (subarr + 1))/2 - subarr;
            subarr = 1;
        }
        
        return total;
    }
};
