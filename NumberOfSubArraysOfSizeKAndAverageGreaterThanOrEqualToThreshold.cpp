class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {
        int n = arr.size();
        int left = 0 , right = 0;
        int num = 0;
        double sum = 0;
        int counter = k;
        
        while(right < n)
        {
            if(counter <= 0)
            {
                sum -= arr[left];
                left++;
            }
            
            sum += arr[right];
            right++;
            counter--;
            if(sum/k >= threshold && counter <= 0)
                num++;
        }
        
        return num;
    }
};
