#include<iostream>
// #include<climits>
using namespace std;
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
    for(int i=0;i<n;i++)
    {
        int c=0;
        for(int j=0;j<n;j++)
        {
            if(arr[i]==arr[j])
            {
                c+=1;
            }
        }
        // cout<<arr[i]<<" majority in array is = "<<c<<endl;
        if(c>(n/2))
        {
            cout<<" majority in array is = "<<arr[i];
            return 0;
        }
    }
    cout<<"No majority elements"; 
}