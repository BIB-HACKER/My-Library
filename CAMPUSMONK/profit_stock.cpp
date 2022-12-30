// you are given an array prices where prices[i] is the price of a gicen stock on the i^th day.

// you want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

// reurn the maximum profit you can achive from this transaction. if you cannot achive any profit, return 0.

#include<iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int p[n];
    for(int i=0;i<n;i++)
    {
        cin>>p[i];
    }

    int prof=0;
    for(int i=0;i<n;i++)
    {
        for(int j=1;j<n-i;j++)
        {
            int val = p[n-j]-p[i];
            if (val>prof)
            {
                prof=val;
            }
        }
    }
    cout<<"output is = "<<prof;
    return 0;
}