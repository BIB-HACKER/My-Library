#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    //# 2ND MAXIMUM NUMBER FIND IN ARRAY
    int n; cin>>n;
    int arr[n];
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    int mx=arr[0];
    for(int i=0;i<n;i++)
    {
        if(arr[i]>mx)
        {
            mx=arr[i];
        }
    }
    int second_max = INT8_MIN; //(INT8_MIN=-128)  OR (INT8_MAX=127)
    for(int i=0;i<n;i++)
    {
        if(arr[i] != mx)
        {
            if(arr[i]>second_max)
            {
                second_max=arr[i];
            }
        }
    }
    cout<<"2nd maximum number is = "<<second_max<<endl;


    //# 2ND MINIMUM NUMBER FIND IN ARRAY
    // int n; cin>>n;
    // int arr[n];
    // for(int i=0;i<n;i++)
    // {
    //     cin>>arr[i];
    // }
    // int mn=arr[0];
    // for(int i=0;i<n;i++)
    // {
    //     if(arr[i]>mn)
    //     {
    //         mn=arr[i];
    //     }
    // }
    // int second_min = INT_MIN;
    // for(int i=0;i<n;i++)
    // {
    //     if(arr[i] != mn)
    //     {
    //         if(arr[i]>second_min)
    //         {
    //             second_min=arr[i];
    //         }
    //     }
    // }
    
    // int n=5;
    // int arr[n]={11,22,33,44,55};
    // // for(int i=0;i<n;i++)
    // // {

    // // }
    // cout<<INT8_MIN;
}