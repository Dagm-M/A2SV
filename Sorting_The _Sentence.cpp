class Solution {
public:
    string sortSentence(string s) {
       string arr[10];
    int j = 0;
    int counter = 0;
    for (int i = 0; i < s.length(); i++)
    {
        if (int(s[i]) == 32)
        {
            int len = i - j;
            int x = int(s[i - 1]) - int('0');
            arr[x] = s.substr(j, len - 1);
            j = i + 1;
            counter++;
        }
    }
    int y = int(s[s.length() - 1]) - int('0');
    arr[y] = s.substr(j);
    arr[y] = s.substr(j, arr[y].length() - 1);

    string n;

    for (int i = 1; i <= counter; i++)
    {
        n.append(arr[i]);
        n.append(" ");
    }
    
    n.append(arr[counter +1]);
        
    return n;
        
    }
};
