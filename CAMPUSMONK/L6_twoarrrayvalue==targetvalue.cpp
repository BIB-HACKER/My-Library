#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    cout<<"enter array size =";
    int n; cin>>n;
    int arr[n];
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    cout<<"enter target value =";
    int target; cin>>target;

    for(int j=0;j<n;j++)
    {
        for(int i=j+1;i<n;i++)
        {
            if(arr[j]+arr[i]==target)
            {
                cout<<"Yes"<<endl;
                return 0;
            }
        }
    }
    cout<<"No"<<endl;

}
