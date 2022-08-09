class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        int top,top2;
        int n = stones.size();
        make_heap(stones.begin(),stones.end());
        while(n > 1)
        {
            top = stones[0];
            pop_heap(stones.begin(),stones.end());
            stones.pop_back();
            top2 = stones[0];
            pop_heap(stones.begin(),stones.end());
            stones.pop_back();
            if(top - top2 != 0)
            {
                stones.push_back(top - top2);
                push_heap(stones.begin(),stones.end());
            }
            n = stones.size();
        }
        if(stones.empty())
            return 0;
        return stones[0];
    }
};
