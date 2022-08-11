class Solution {
public:
    string decodeString(string s) {
        stack <string> st;
        int n = s.size();
        string str = "";
        string si = "";
        int size;
        
        for(int i=0 ; i < n ; i++)
        {
            str = "";
            if(s[i] != ']')
            {
                si = s[i];
                st.push(si);
            }
            else
            {
                while(st.top()[0] != '[')
                {
                    str = st.top() + str;
                    st.pop();
                }
                st.pop();
                

                
                si = "";
                while(!st.empty() && isdigit(st.top()[0]))
                {
                    si = st.top() + si;
                    st.pop();
                }
                
                if(!si.empty())
                {
                    size = stoi(si);
                    for(int j = 0; j < size ; j++)
                        st.push(str);
                }
                
            }
        }
        si = "";
        while(!st.empty())
        {
            si = st.top() + si;
            st.pop();
        }

        
        return si;
    }
};
    
