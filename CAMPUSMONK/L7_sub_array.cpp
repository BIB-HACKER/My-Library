// #include<bits/stdc++.h>
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
        cin>>arr[i];            // [1,2,3,4,5]
    }
    cout<<"Target value =";
    int target; cin>>target;
    for(int i=0;i<n;i++)     // [1,2,3,4,5]
    {                  // index= 0 1 2 3 4
        int sum=0;
        for(int j=i;j<n;j++)   // [1,2,3,4,5]
        {
            sum+=arr[j];   // sum+= 1+       == target
            if(sum==target)       //1+2      == target
            {                     //1+2+3    == target
                cout<<"yes"<<endl;//1+2+3+4  == target
                return 0;         //1+2+3+4+5== target   
            }
        }
    }
    cout<<"Not found";
}