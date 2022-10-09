class Solution {
public:
    int maxVowels(string s, int k) {
        int n = s.size();
        int left = 0, right = 0;
        int numVowel = 0;
        int maxVowel = 0;
        unordered_set<char> vowel;
        
        vowel.insert('a');
        vowel.insert('e');
        vowel.insert('i');
        vowel.insert('o');
        vowel.insert('u');
        
        while(right < n)
        {
            if(k <= 0)
            {
                if(vowel.find(s[left]) != vowel.end())
                    numVowel--;
                left++;
            }
            
            if(vowel.find(s[right]) != vowel.end())
                numVowel++;
            right++;
            k--;
            maxVowel = max(maxVowel, numVowel);
        }
        
        return maxVowel;
    }
};
