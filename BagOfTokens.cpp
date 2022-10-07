class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        sort(tokens.begin(),tokens.end());
        int score = 0;
        int n = tokens.size();
        int i = 0, j = n -1;
        
        if(n == 0)
            return 0;
            
        while(i < j)
        {
            if(power < tokens[i] && score > 0)
            {
                power += tokens[j];
                score--;
                j--;
            }
            
            else if(power >= tokens[i])
            {
                power -= tokens[i];  
                score++;
                i++;
            }
            else
                break;
        }
        

        if(power >= tokens[i])
            score++;
        
        return score;
        
    }
};
