class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> map;
        int n = nums.size();
        vector<vector<int>> v;
        vector<int> vec;
        
        for(int i = 0 ;i < n ; i++)
            map[nums[i]]++;
        
        for (auto x : map)
        {
            vec.push_back(x.second);
            vec.push_back(x.first);
            v.push_back(vec);
            vec.clear();
        }
        
        make_heap(v.begin(),v.end());
        sort_heap(v.begin(),v.end());
        
        
        while(k != 0)
        {
            n = v.size();
            vec.push_back(v[n-1][1]);
            v.pop_back();
            k--;
        }
        
       
        return vec;
    }
};
