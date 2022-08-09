class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        
        vector<int> out;
        bool check = true;
        
        for(int i =0; i<n; i++)
        {
            int m = nums2.size();
            check = true;
            for(int j=0; j < m ; j++)
            {
                if(nums1[i] == nums2[j])
                {
                    for(int k = j; k < m ; k++)
                    {
                        if((k == m-1)?false : nums1[i] < nums2[k + 1])
                        {
                            out.push_back(nums2[k+1]);
                            check = false;
                            break;
                        }   
                    }
                    
                     if(check)
                        out.push_back(-1);
                    
                    break;
                }
            }
        }
        return out;
    }
};
