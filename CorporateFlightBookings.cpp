class Solution {
public:
    vector<int> corpFlightBookings(vector<vector<int>>& bookings, int n) {
        vector<int> v(n,0);
        int bsize = bookings.size();
        
        for(int i = 0; i < bsize; i++)
        {
            v[bookings[i][1] - 1] += bookings[i][2];
            if(bookings[i][0] - 2 >= 0)
               v[bookings[i][0] - 2] -= bookings[i][2];
        }
        
        for(int i = n-2 ; i >= 0; i--)
            v[i] += v[i+1];
        
        return v;
    }
};
