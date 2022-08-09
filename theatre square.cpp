#include <iostream>

using namespace std;

int main(){
    long long m,n,a;
    cin>>m;
    cin>>n;
    cin>>a;
    long long counter = 0;
    if(m<=a && n<=a)
    {
        counter++;
    }
    else
    {
        long long x;
        if(m%a == 0)
        {
            x = m/a;
            counter = x;
            if(n%a == 0)
            {
                x = n/a;
                counter *= x;
            }
            else
            {
                x = (n/a) + 1;
                counter *= x;
            }
        }
        else
        {
            x = (m/a)+1;
            counter = x;
            if(n%a == 0)
            {
                x = n/a;
                counter *= x;
            }
            else
            {
                x = (n/a) + 1;
                counter *= x;
            }
        }
    }
    cout<<counter;
}
