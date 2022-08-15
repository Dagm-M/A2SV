class Solution {
public:
    string BitString(int n, string s)
    {
        if(n == 0)
            return s;
        int a = s.size();
        string st = s;
        for(int i = 0 ; i < a ; i++)
        {
            if(st[i] == '0')
                st[i] = '1';
            else if(st[i] == '1')
                st[i] = '0';
        }
        for (int i = 0; i < a / 2; i++)
            swap(st[i], st[a - i - 1]);
        
        s = s + "1" + st;
        return BitString(--n, s);
    }
    
    char findKthBit(int n, int k) {
        string s = "0" ;
        s = BitString(n,s);
        return s[k-1];
    }
};
