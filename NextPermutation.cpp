class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size();
        bool swiched = false;
        int position = 0;
        if(n == 1)
            return;
        int left = n-2;
        int right = n-1;
       
        while(left >= 0)
        {
            if(nums[left] < nums[right])
            {
                int temp = nums[left];
               
                int largest = right;
                while(right < n)
                {
                    if(nums[right] > nums[left] && nums[right] < nums[largest])
                        largest = right;
                    right++;
                }
                
                nums[left] = nums[largest];
                nums[largest] = temp;
                
                position = left + 1;
                break;
            }
            else
                right--;
            
            left--;
        }
        
        sort(nums.begin() + position, nums.end());
        
        
    }
};
