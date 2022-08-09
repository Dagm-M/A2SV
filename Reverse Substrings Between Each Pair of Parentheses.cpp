class Solution {
public:
    string reverseParentheses(string s) {
        vector<char> first;
        vector<char> second;
        string answer;

        
        for(int i = 0 ; i < s.size() ; i++)
        {
            second.clear();
            first.push_back(s[i]);
            if(s[i] == ')')
            {
                first.pop_back();
                for(int j = first.size()-1 ; first[j] != '(' ; j--)
                {
                    second.push_back(first[j]);
                    first.pop_back();
                }
                first.pop_back();
                for(int j = 0 ; j < second.size() ; j++)
                    first.push_back(second[j]);
            }
        }
        

        
        for(int j = 0 ; j < first.size() ; j++)
        {
            answer += first[j];
        }

        
        return answer;
    }
};
