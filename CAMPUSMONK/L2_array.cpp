#include<iostream>
using namespace std;
int main()
{
    // int arr[10]={2,4,7,9,1,2,8};
    // for(int i=0;i<10;i++)
    // {
    //     cout<<arr[i]<<endl;
    // }

    // INPUT
    int size; cin>>size;
    int arr[size];
    for(int i=0; i<size; i++)
    {
        cin>>arr[i];
    }
    // OUTPUT
    int sum=0;
    for(int i=0; i<size; i++)
    {// SUM OF ARRAY
        sum=sum + arr[i];
    // MULTIPLICATION OF ARRAY
        // sum=sum * arr[i];
   
    }
     
    // cout<<sum;
     // AVG OF AN ARRAY?       
    cout<<(sum/size)<<endl;
    cout<<(float(sum)/size)<<endl;  // FLOAT>INTIGER

}
