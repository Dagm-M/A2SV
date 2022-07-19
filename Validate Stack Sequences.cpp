class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        int i = 0, j=0,n;
        while(true)
        {
            n = pushed.size();
            if(pushed[i] != popped[j] && n-1 != i)
                i++;
            else if(pushed[i] == popped[j])
            {
                
                pushed.erase(pushed.begin() + i);
                j++;
                n= pushed.size();
                if(i > 0 || n == 0)
                    i--;
                if(i < 0)
                    break;
            }
            else
                break;
        }

        return pushed.empty();
    }
};
