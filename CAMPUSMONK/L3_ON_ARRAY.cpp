#include<iostream>
using namespace std;
int main()
{
    //find minimum element form array     arr[size]={4,57,789,2}
    int n; cin>>n;
    int arr[n];
    // cin>>arr[]
    for(int i=0; i<n; i++)
    {
        cin>>arr[i];
    }

    // output --> min element from the array
    int mn=arr[0];
    for(int i=0; i<n; i++)
    {
        if(mn>arr[i])
        {
            mn=arr[i];
        }
    }
    cout<<mn<<endl;
}

///////////////////////////////////////////////////////////////////////////

#include<iostream>
using namespace std;
int main()
{
    //find maximum element form array     arr[size]={4,57,789,2}
    int n; cin>>n;
    int arr[n];
    // cin>>arr[]
    for(int i=0; i<n; i++)
    {
        cin>>arr[i];
    }
    // array -> itreate and traverse are same
    int mx=arr[0];
    for(int i=0; i<n; i++)
    {
        if(mx<arr[i])
        {
            mx=arr[i];
        }
    }
    // cout<<mx<<endl;


    
    int x; cin>>x;
    for(int i=0; i<n;i++)
    {
        if(arr[i]==x)
        {
            cout<<"True"<<endl;
            return 0;
        }
    }
    cout<<"False"<<endl;
}
