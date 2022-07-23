class KthLargest {
private:
    vector<int> nums;
    int k;
public:
    KthLargest(int k, vector<int>& nums) {
        this -> k = k;
        this -> nums = nums;
        make_heap(this -> nums.begin(),this -> nums.end(),greater());
    }
    
    int add(int val) {
        nums.push_back(val);
        push_heap(nums.begin(),nums.end(),greater());
        int n = nums.size();

        for(int i = n ; i > k; i--)
        {
            pop_heap(nums.begin(),nums.end(),greater());
            nums.pop_back();
        }

        return nums[0];
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */
