#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    int n; cin>>n;
    int arr[n];
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }

    // reverse array
    reverse(arr, arr+n);
    for(int i=0; i<n;i++)
    {
        cout<<arr[i]<<" "<<endl;
    }

    // sort array
    sort(arr, arr+n);
    // min, max
    cout<<"min = "<<arr[0]<<endl;
    cout<<"max = "<<arr[n-1]<<endl;
    // kth min, kth max
    cout<<"kth min = "<<arr[0+1]<<endl;
    cout<<"kth max = "<<arr[n-2]<<endl;
    
    
}