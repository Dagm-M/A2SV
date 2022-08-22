class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        int n = fruits.size();
        if(n < 2)
            return 1;
        int fruit1 = fruits[0];
        int fruit2 = fruits[0];
        int sum = 0;
        
        
        int a = 0 , b = 1, c = 0;
        
        while(b < n)
        {
            if(fruit1 == fruit2)
            {
                c = b;
                fruit2 = fruits[b];
            }
            
            if(fruits[b] == fruit1 || fruits[b] == fruit2)
            {
                if(fruits[b] != fruits[c])
                    c = b;
                sum = max(b-a+1,sum);
            }
            else
            {
                a = c ;
                c = b;
                fruit1 = fruits[a];
                fruit2 = fruits[b];
            }
            b++;
        }
        
        return sum;
    }
};
