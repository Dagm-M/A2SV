class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        stack<int> s;
        vector<int>gap;
        
        for(int i= n-1 ; i>= 0 ;i--)
        {
            while(!s.empty() && temperatures[i] >= temperatures[s.top()])
                s.pop();
            
            if(s.empty())
                gap.push_back(0);
            else if(temperatures[i] < temperatures[s.top()])
                gap.push_back(s.top() - i);
            
            s.push(i);
        }
        
        reverse(gap.begin(),gap.end());
        
        return gap;
    }
};
