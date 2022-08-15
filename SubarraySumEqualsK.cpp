class Solution {
public:
int subarraySum(vector<int> &nums, int k)
{
    int n = nums.size();
    unordered_map<int, int> prefixSum;
    int sum = nums[0];
    prefixSum[sum] += 1;
    int answer = 0;

    if (sum == k)
        answer++;

    for (int i = 1; i < n; i++)
    {
        sum += nums[i];
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
