class Solution {
public:
    
    int winner(vector<int> vec, int k, int beg)
    {
        if(vec.size() == 1)
            return vec[0];
        
        if(beg + (k-1) < vec.size())
        {
            beg = beg + (k-1);
            vec.erase(vec.begin() + beg);
        }
        else
        {
            beg = (k-1) - (vec.size() - beg);
            while(beg >= vec.size())
                beg -= vec.size();
            vec.erase(vec.begin() + beg);
        }
        
        return winner(vec, k , beg);
        
    }
    
    int findTheWinner(int n, int k) {
        vector<int> vec(n);
        iota(vec.begin(), vec.end(), 1);
        return winner(vec, k, 0);
    }
    

};
