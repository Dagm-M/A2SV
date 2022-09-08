class Solution {
public:
    int hIndex(vector<int>& citations) {
        sort(citations.begin(),citations.end());
        int n = citations.size();
        int count = 0;
        for(int i = n-1 ; i >= 0 ; i--)
        {
            count++;
            if(count > citations[i])
            {
                count--;
                break;
            }
        }
        
        
        return count;
    }
};
