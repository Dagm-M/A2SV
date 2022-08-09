class Solution {
public:
    bool isValid(string s) {
    vector<char> stack;
    int a;
    int place = 0;
    int n = s.size();
    for (int i = 0; i < n; i++)
    {
        stack.push_back(s[i]);
    }
    n = stack.size();
    for (int i = 1; i < n; i++)
    {
        if (int(stack[place]) == 40)
            a = 1;
        else
            a = 2;

        if (int(stack[place]) + a == int(stack[i]))
        {
            stack.erase(stack.begin() + place);
            stack.erase(stack.begin() + i - 1);
            place = 0;
            n = stack.size();
            i = 0;
        }
        if (int(stack[i]) == 40 || 91 || 123)
            place = i;
        else
            break;
    }
    return stack.empty();
    }
};
