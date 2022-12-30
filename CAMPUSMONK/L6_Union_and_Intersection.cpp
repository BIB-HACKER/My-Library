#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    cout<<"enter array1 size =";
    int n1; cin>>n1;
    int arr1[n1];
    for(int i=0;i<n1;i++)
    {
        cin>>arr1[i];
    }

    cout<<"enter array2 size =";
    int n2; cin>>n2;
    int arr2[n2];
    for(int i=0;i<n2;i++)
    {
        cin>>arr2[i];
    }
    // Union
    // for(int i=0;i<n1;i++)
    // {
    //     cout<<arr1[i]<<" ";
    // }
    // for(int i=0;i<n2;i++)
    // {
    //     bool present=false;
    //     for(int j=0;j<n1;j++)
    //     {
    //         if(arr2[i]==arr1[j])
    //         {
    //             present=true;
    //         }
    //     }
    //     if(present==false)
    //     {
    //         cout<<arr2[i]<<" ";
    //     }
    // }
    // intersection
    for(int i=0;i<n1;i++)
    {
        for(int j=0;j<n2;j++)
        {
            if(arr1[i]==arr2[j])
            {
                cout<<"intersection ->"<<arr1[i]<<" ";
            }
        }
    }
}