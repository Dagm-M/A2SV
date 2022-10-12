// class Solution {
// public:
//     int BinaryToDecimal(string str) {
//         int dec = 0;
//         int len = str.size();

//         for(int i = len -1 ; i >= 0; i--)
//         {
//             if(str[i] == '1')
//                 dec += pow(2,(len-1) - i);
//         }
            
//         return dec;
//     }
    
//     string DecimalToBinary(int dec)
//     {
//         int remainder;
//         string binary;

//         while (dec != 0) 
//         { 
//             remainder = dec % 2;
//             binary = to_string(remainder) + binary;
//             dec = dec / 2;
//         }
        
//         return binary;
//     }
    
//     string Xor(string b1,string b2)
//     {
//         if(b1.size() > b2.size())
//         {
//             for(int i = b1.size() - 1 , j = b2.size() - 1; j >= 0; i--, j--)
//             {
//                 if(b1[i] xor b2[j])
//                     b1[i] = '1';
//                 else
//                     b1[i] = '0';
//             }
            
//             return b1;
//         }
        
//         else
//         {
//             for(int i = b1.size() - 1 , j = b2.size() - 1; i >= 0; i--, j--)
//             {
//                 if(b2[j] xor b1[i])
//                     b2[j] = '1';
//                 else
//                     b2[j] = '0';
    
//             }
            
           
//             return b2;
//         }
//     }
    
    
    
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        vector<int> answer;
        
        
    
        for(int i = 1 ; i<arr.size() ; i++)
            arr[i] ^= arr[i-1];
        
        for(int i = 0 ;i < queries.size(); i++)
        {
            if(queries[i][0] > 0)
                answer.push_back(arr[queries[i][0] -  1]^ arr[queries[i][1]]);
            else
                answer.push_back(arr[queries[i][1]]);
        }
        
        return answer;
    }
};
