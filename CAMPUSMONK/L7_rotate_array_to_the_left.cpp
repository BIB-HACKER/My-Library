#include<bits/stdc++.h>
using namespace std;
void left_rotate(int arr[], int n)
{
    int save=arr[0];
    for(int i=0;i<n-1;i++)
    {
        arr[i]=arr[i+1];
    }
    arr[n-1] = save;
}
int main()
{
    cout<<"array size =";
    int n; cin>>n;
    int arr[n];
    for(int i=0;i<n;i++)
    {
        cout<<"input value =";
        cin>>arr[i];
    }
    cout<<"rotate array time =";
    int k; cin>>k;
    for(int i=0;i<k;i++)
    {
        left_rotate(arr,n);
    }
    for(int i=0;i<n;i++)
    {
        cout<<arr[i]<<" ";
    }
}