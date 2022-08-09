class Solution
{
public:
    string removeKdigits(string num, int k)
    {
        int n = num.size();
        stack<char> mystack;

        for (int i = 0; i < n; i++)
        {
            while (!mystack.empty() && k > 0 && mystack.top() > num[i])
            {
                mystack.pop();
                k -= 1;
            }
            if (!mystack.empty() || num[i] != '0')
                mystack.push(num[i]);
        }

        while (!mystack.empty() && k--)
            mystack.pop();

        if (mystack.empty())
            return "0";

        while (!mystack.empty())
        {
            num[n - 1] = mystack.top();
            mystack.pop();
            n -= 1;
        }
        return num.substr(n);
    }
};
