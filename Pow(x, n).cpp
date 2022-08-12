class Solution {
public:
    double myPow(double x, int n) {
        double answer;
        
        if(n == 0)
            return 1;
        if(n == 1)
            return x;
        if(n == -1)
            return 1/x;
        if(x == 1)
            return 1;
        
        if(n%2 == 0)
        {
            answer = x * x;
            answer = myPow(answer, n/2);
        }
        else
        {
            if(n > 0)
            {
                answer = x * x;
                answer = myPow(answer, n/2) * x;
            }
            else
            {
                answer = x * x;
                answer = myPow(answer, n/2) * 1/x;
            }
        }
        
        
        return answer;
    }
};
