#include<iostream>
using namespace std;
int main()
{
    // rotate the array by 1 position on the right
    // [3,2,1,0]---input
    // [0,3,2,1]---output
    int n; cin>>n;
    int arr[n];
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }

    int last=arr[n-1];
    for(int i=n-1; i>0; i--)
    {
        arr[i]=arr[i-1];
    }
    arr[0]=last;

    for(int i=0; i<n; i++)
    {
        cout<<arr[i]<<" ";
    }

}