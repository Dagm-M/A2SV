class Solution {
public:
    int minSetSize(vector<int>& arr) {
        unordered_map<int, int> map;
        int n = arr.size();
        vector<int> v;
        for(int i = 0 ;i < n ; i++)
            map[arr[i]]++;
        
        for (auto x : map)
            v.push_back(x.second);
        
        sort(v.begin(),v.end());

        int sum = 0;
        int counter = 0;
        

        while(sum < n/2)
        {
            sum += v.back();
            v.pop_back();
            counter++;
        }
        
        return counter;
    }
};
