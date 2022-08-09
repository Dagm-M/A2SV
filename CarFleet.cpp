<<<<<<< HEAD
class Solution
{
public:
    int carFleet(int target, vector<int> &position, vector<int> &speed)
    {
        vector<vector<double>> vec;
        int n = position.size();
        stack<double> s;
        double time;

        for (int i = 0; i < n; i++)
        {

            vector<double> v1;

            v1.push_back(position[i]);
            v1.push_back(speed[i]);

            vec.push_back(v1);
        }

        sort(vec.begin(), vec.end());

        for (int i = n - 1; i >= 0; i--)
        {
            time = (target - vec[i][0]) / vec[i][1];

            if (s.empty())
                s.push(time);
            else if (s.top() < time)
                s.push(time);
        }
        return s.size();
    }
=======
class Solution
{
public:
    int carFleet(int target, vector<int> &position, vector<int> &speed)
    {
        vector<vector<double>> vec;
        int n = position.size();
        stack<double> s;
        double time;

        for (int i = 0; i < n; i++)
        {

            vector<double> v1;

            v1.push_back(position[i]);
            v1.push_back(speed[i]);

            vec.push_back(v1);
        }

        sort(vec.begin(), vec.end());

        for (int i = n - 1; i >= 0; i--)
        {
            time = (target - vec[i][0]) / vec[i][1];

            if (s.empty())
                s.push(time);
            else if (s.top() < time)
                s.push(time);
        }
        return s.size();
    }
>>>>>>> 5d19fe112cd221cffcaaebadd9fda5e144a468b0
};