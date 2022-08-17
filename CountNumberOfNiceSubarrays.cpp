class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        
        int n = nums.size();
        unordered_map<int, int> prefixSum;
        int sum = (nums[0] % 2 == 0)?0:1;
        prefixSum[sum] += 1;
        int answer = 0;

        if (sum == k)
            answer++;

        for (int i = 1; i < n; i++)
        {
            sum += (nums[i] % 2 == 0)?0:1;
            if (prefixSum.find(sum - k) != prefixSum.end())
                answer += prefixSum[sum - k];

                    prefixSum[sum] += 1;

            if (sum == k)
            {
                answer++;
                continue;
            }
        }

        return answer;
        
    }
};
