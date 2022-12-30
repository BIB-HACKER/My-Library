#include<iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }

    int cnt=0;

    for (int i=0;i<n;i++)
    {
        // if(a[i]/2==0)
        // {
        //    a[i]= (a[i])-1/2;
        //     cnt++;
        // }
        // else
        // {
        //     a[i]=(a[i]/2);
        //     cnt++;
        // }
        while(a[i]>0)
        {
            a[i]=a[i]/2;
            cnt++;
        }
    }

    cout<<"output is -> "<<cnt;
    return 0;
}