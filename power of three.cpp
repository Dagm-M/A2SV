class Solution {
public:
    bool powerOfThree(double n)
    {
        if(n == 1)
            return true;
        else if(n == 0)
            return false;
        else
            return powerOfThree(n/3);
    }
    
    bool isPowerOfThree(int n) {
        return powerOfThree(n);
    }
};
