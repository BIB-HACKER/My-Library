#include<iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++)
    {
        cin>>a[i]; // a[11,1,8,12,14]
    }

    bool dif=false;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            if((a[i]-a[j]==1)||(a[j]-a[i]==1))
            {
                dif=true;
                break;
            }
        }
    }
    cout<<dif;
    return 0;
}