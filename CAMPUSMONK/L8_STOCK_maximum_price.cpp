#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    cout<<"array size = ";
    int n; cin>>n;
    int arr[n];
    for(int i=0;i<n;i++)
    {
        cout<<"input stock price -> ";
        cin>>arr[i];   //arr[9,12,15,8,2]
    }

    int max_profit=0;
    for(int i=0;i<n;i++)
    {
        // int buying_price=arr[i];
        for(int j=i+1;j<n;j++)
        {
            // int selling_price = arr[j];
            // if(selling_price - buying_price > max_profit)
            // {
            //     max_profit=selling_price - buying_price;
            // }
            max_profit = max(max_profit, arr[j] - arr[i]);
        }
    }
    cout<<"maximum profit is -->"<<max_profit<<endl;
}