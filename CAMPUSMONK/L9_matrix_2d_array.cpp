#include<iostream>
using namespace std;
int main()
{
    int n,m; cin>>n>>m;
    int matrix[n][m];
    for(int i=0;i<m;i++)
    {
        for(int j=0;j<m;j++)
        {
            cin>>matrix[i][j];
        }
    }
    for(int i=0;i<m;i++)
    {
        for(int j=0;j<m;j++)
        {
            cout<<matrix[i][j]<<" ";
        }
        cout<<endl;
    }
}
