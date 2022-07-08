class Solution {
public:
    
    int pop(vector<int> &stack, int i) 
    {
    int a = stack[i];
    stack.erase(stack.begin() + i);
    return a;
    }
    
    
    int evalRPN(vector<string>& tokens) {
        int n = tokens.size();
        int a, b;
        vector<int> stack;
        for (int i = 0; i < n; i++)
        {
            int s = stack.size();
            if (tokens[i] == "+")
            {

                // cout << stack[s - 1] << endl;
                a = pop(stack, s - 1);
                // cout << "second " << stack[s - 2] << endl;
                b = pop(stack, s - 2);
                stack.push_back(a + b);
            }
            else if (tokens[i] == "-")
            {
                a = pop(stack, s - 1);
                b = pop(stack, s - 2);
                stack.push_back(b - a);
            }
            else if (tokens[i] == "*")
            {
                a = pop(stack, s - 1);
                b = pop(stack, s - 2);
                stack.push_back(a * b);
            }
            else if (tokens[i] == "/")
            {
                a = pop(stack, s - 1);
                b = pop(stack, s - 2);
                stack.push_back(b / a);
            }
            else
                stack.push_back(stoi(tokens[i]));
        }
                    
        return stack[0];
                    
        
    }
};
