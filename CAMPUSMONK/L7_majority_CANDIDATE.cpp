#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    cout<<"array size =";
    int n; cin>>n;
    int arr[n];
    for(int i=0;i<n;i++)
    {
        cout<<"input value =";
        cin>>arr[i];   // [5,3,5,9,5,20,5]
    }
    sort(arr, arr+n);   // [3,3,5,5,5,9,20,5]
    int middile=arr[n/2];
    int cnt=0;
    for(int i=0;i<n;i++)
    {
        if(arr[i]==middile)
        {
            cnt++;
        }
    }
    if(cnt>(n/2))
    {
        cout<<"majority element found :"<<middile<<endl;
    }
    else{
        cout<<"no majority element found :";
    }
}