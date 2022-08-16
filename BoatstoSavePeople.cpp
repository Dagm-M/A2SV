class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
       
        int total = 0;
        int n = people.size();
        int a = 0 ,b = n-1;
        sort(people.begin(),people.end());
        
        while(a <= b)
        {
            if(people[a] + people[b] <= limit)
            {
                total ++;
                a++;
                b--;
            }
            else if(people[a] > people[b])
            {
                a++;
                total++;
            }
            else
            {
                b--;
                total++;
            }
                
        }
        
        return total;
    }
};
