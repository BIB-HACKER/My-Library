// INPUT : 1 14 11 51 15, LOW=50, HIGH=55
// OUTPUT : 50 52 52 54 55
#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int a[n];

    for(int i=0;i<n;i++)
    {
        cin >> a[i];
    }
    int low,high;
    cin >> low >> high;

    sort(a,a+n);
    int i=0;

    while(a[i]<low)
    {
        i++;
    }
    while(low<a[i])
    {
        cout<<low;
        low++;
    }
    return 0;
}