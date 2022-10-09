class Solution {
public:
    int threeSumMulti(vector<int>& arr, int target) {
        int n = arr.size();
        unordered_map<int,int> m;
        unordered_set<int> inner;
        int k;
        long total = 0;
        int mod = (pow(10,9) + 7);
        
        for(int i = 0 ;i<n ;i++)
            m[arr[i]]++;
        
        for(int i = 0; i<n ;i++)
        {
            if(m[arr[i]] > 1)
                m[arr[i]]--;
            else
                m.erase(arr[i]);
            
            for(int j = i+1; j < n; j++)
            {
                
                if(inner.find(arr[j]) != inner.end())
                    continue;
                
                k = target - arr[i] - arr[j];

                if(m.find(k) != m.end())
                {
                    if(arr[j] != k)
                        total += (m[arr[j]] * m[k]);
                    else
                        total += (m[k]*(m[k]-1))/2;
                    
                    inner.insert(arr[j]);
                    inner.insert(k);
                }
            }
            inner.clear();
        }
        
        return (int)(total % mod);
    }
};
