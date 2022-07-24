class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        int n = heights.size();
        vector<int> previous;
        int difference;
        int counter = 0;
        int i;
        
        if(n-1 <= ladders)
            return n-1;
        
        for(i = 0 ; i<n-1; i++)
        {
            if(heights[i] >= heights[i+1])
            {
                counter ++;
                continue;
            }
            
            difference = heights[i+1] - heights[i];
            previous.push_back(difference);
            push_heap(previous.begin(),previous.end(),greater());
            
            if(previous[0] > bricks && previous.size() > ladders)
                break;
            
            if(previous.size() > ladders)
            {
                if(previous[0] <= bricks)
                {
                    counter ++;
                    bricks -= previous[0];
                    pop_heap(previous.begin(),previous.end(),greater());
                    previous.pop_back();
                }
            }
            
        }
        
        if(n-1 < counter + ladders)
            return n-1;
        else
             return counter + ladders;
        
    }
};
