class Solution {
private:
    bool priority(char a, char b)
    {
        if((a == '*' || a == '/') && (b == '*' || b == '/'))
            return false;
        
        if((a == '+' || a == '-') && (b == '+' || b == '-'))
            return true;
        
        if((a == '/' || a == '*') && (b == '+' || b == '-'))
            return false;
        else
            return true;
    }
    
    string Compute(char c, int a, int b)
    { 
            if(c == '+')
                return to_string(a+b);
            if(c == '-')
                return to_string(a-b);
            if(c == '*')
                return to_string(a*b);
            if(c == '/')
                return to_string(a/b);
            
            return "1";
    }
    
    
public:
    int calculate(string s) {
        string m;
        m = s[0];
        vector<string> num;
        num.push_back(m);
        vector<char> oper;
        int n = s.size();
        int a,b;
        bool isnum = true;
        
        
        for(int i = 1 ; i < n ; i++)
        {
            if(s[i] == ' ')
                continue;
            if(s[i] == '*' || s[i] == '/' || s[i] == '+' || s[i] == '-')
            {
                if(oper.size() > 0)
                {
                    if(priority(oper.back(), s[i]))
                    {
                        oper.push_back(s[i]);
                    }
                    
                    else
                    {
                        a = stoi(num.back());
                        num.pop_back();
                        b = stoi(num.back());
                        num.pop_back();
                        num.push_back(Compute(oper.back(), b , a));
                        oper.pop_back();
                        oper.push_back(s[i]);
                    }
                }
                
                else
                    oper.push_back(s[i]);
                isnum =false;
            }
            
            else
            {
                if(isnum)
                {
                    m = s[i];
                    m = num.back() + m;
                    num.pop_back();
                    num.push_back(m);
                }
                
                else
                {
                    m = s[i];
                    num.push_back(m);
                }
                isnum = true;
            }
        }
        
        if(num.size() != 1 && (oper.back() == '*' || oper.back() == '/'))
        {
            a = stoi(num.back());
            num.pop_back();
            b = stoi(num.back());
            num.pop_back();
            num.push_back(Compute(oper.back(), b , a));
            oper.pop_back();
        }
            reverse(num.begin(),num.end());
            reverse(oper.begin(),oper.end());

        
        while(num.size() != 1)
        {
            a = stoi(num.back());
            num.pop_back();
            b = stoi(num.back());
            num.pop_back();
            num.push_back(Compute(oper.back(), a , b));
            oper.pop_back();
        }

        
        return stoi(num.back());
    }
    
    
};
