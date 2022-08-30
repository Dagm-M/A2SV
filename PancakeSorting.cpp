class Solution {
public:
    vector<int> pancakeSort(vector<int>& arr) {
        vector<int> pan;
        int n = arr.size();
        int i = n-1;
        
        while(i >= 0)
        {
            if(i == 0 && arr[i] == 1)
                break;
            
            if(arr[i] == n)
            {
                if((i+1) == arr[i])
                {
                    i--;
                    n--;
                    continue;
                }
                reverse(arr.begin(),arr.begin() + i+1);
                pan.push_back(i+1);
                reverse(arr.begin(),arr.begin()+ n);
                pan.push_back(n);
                n--;
                i = n-1;
            }
            else
                i--;
        }
        
        
        
        return pan;
        
    }
};
