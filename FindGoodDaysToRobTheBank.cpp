class Solution {
public:
    vector<int> goodDaysToRobBank(vector<int>& security, int time) {
        int n = security.size();
        vector<int> goodDaysBefore(n,0);
        vector<int> goodDaysAfter(n,0);
        vector<int> Answer;
        
        for(int i = 1 ; i<n ; i++)
        {
            if(security[i-1] >= security[i])
                goodDaysBefore[i] += goodDaysBefore[i-1] + 1;
        }
        
        for(int i = n-2; i >= 0 ; i--)
        {
            if(security[i + 1] >= security[i])
                goodDaysAfter[i] += goodDaysAfter[i+1] + 1;
        }
        
        for(int i = 0 ; i<n ; i++)
        {
            if(goodDaysBefore[i] >= time && goodDaysAfter[i] >= time)
                Answer.push_back(i);
        }
        
        
        return Answer;
    }
};
