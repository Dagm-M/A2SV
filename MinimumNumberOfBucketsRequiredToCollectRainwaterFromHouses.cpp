class Solution {
public:
    int minimumBuckets(string street) {
        int n = street.size();
        int counter = 0;
        
        if(n == 1 && street[0] == 'H')
            return -1;
        
        for(int i = 0 ; i<n ; i++)
        {
            if(street[i] == 'H')
            {
                if(i == 0)
                {
                    if(street[i+1] == '.')
                    {
                        street[i+1] = 'B';
                        counter++;
                    }
                    else
                        return -1;
                }
                else if(i == n-1)
                {
                    if(street[i-1] == '.')
                    {
                        street[i-1] = 'B';
                        counter++;
                    }
                    else if(street[i-1] == 'H')
                        return -1;
                    else
                        continue;
                }
                else
                {
                    if(street[i+1] == 'B' || street[i-1] == 'B')
                        continue;
                    if(street[i+1] == '.')
                    {
                        street[i+1] = 'B';
                        counter++;
                    }
                    else if(street[i-1] == '.')
                    {
                        street[i-1] = 'B';
                        counter++;
                    }
                    else
                        return -1;
                }
            }
        }
        
        return counter;
    }
};
