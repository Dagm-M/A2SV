class Solution {
public:
    int maxCoins(vector<int>& piles) {
        int n = piles.size();
        int sum = 0;
        sort(piles.begin(),piles.end(),greater());
        for(int j= 0 ,i = 1 ; j < n/3 ; i+=2,j++)
            sum = sum + piles[i];
        return sum;
    }
};
