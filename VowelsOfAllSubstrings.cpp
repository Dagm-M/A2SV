class Solution {
public:
    bool isVowel(char c)
    {
        if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
            return true;
        else
            return false;
    }
    long long countVowels(string word) {
        
        long long sum = 0;
        long long n = word.size();
        
        for(int i = 0 ; i < n ; i++)
        {
            if(isVowel(word[i]))
            {
                if(i == 0 || i == n - 1)
                    sum += n;
                else
                  sum += ((n + (i * (n - (i + 1)))));  
            }
        }
        

        
        return sum;
    }
};
