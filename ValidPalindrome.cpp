class Solution {
public:
    bool isPalindrome(string s) {
        int n = s.size();
        string newS = "";
        for(int i = 0; i < n; i++)
            if(isalpha(s[i]) || isdigit(s[i]))
                newS.push_back(tolower(s[i]));
        int left = 0, right = newS.size()-1;
        cout<<newS<<endl;
        while(left < right)
        {
            if(newS[left] != newS[right])
                return false;
            left++;
            right--;
        }

        return true;
    }
};
