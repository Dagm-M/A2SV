class Solution {
public:
    bool powerOfFour(double n)
    {
        if(n == 1)
            return true;
        else if(n == 0)
            return false;
        else
            return powerOfFour(n/4);
    }
    
    bool isPowerOfFour(int n) {
        return powerOfFour(n);
    }
};
