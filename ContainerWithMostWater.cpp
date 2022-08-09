class Solution
{
public:
    int maxArea(vector<int> &height)
    {
        int n = height.size();
        int maximum = 0;
        int a = 0, b = n - 1;

        int area;
        while (a != b)
        {
            area = (b - a) * min(height[a], height[b]);

            if (area > maximum)
                maximum = area;

            if (height[a] < height[b])
                a++;
            else
                b--;
        }

        return maximum;
    }
};