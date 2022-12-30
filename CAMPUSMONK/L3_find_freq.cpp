#include<iostream>
using namespace std;
int main()
{
    // count the x vlaue in array
    int n; cin>>n;
    int arr[n];
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }

    int x; cin>>x;
    int count=0;
    for(int i=;i<n;i++)
    {
        if(arr[i]==x)
        {
            count=1;
        }
    }
    cout<<count<<endl;
}