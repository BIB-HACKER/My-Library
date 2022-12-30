#include<iostream>
using namespace std;
int main()
{
    int row,col; cin>>row>>col;
    int matrix[row][col];
    for(int i=0;i<row;i++)
    {
        for(int j=0;j<col;j++)
        {
            cin>>matrix[i][j];
        }
    }
    int sum=0;
    for(int i=0;i<row;i++)
    {
        for(int j=0;j<col;j++)
        {
            if(i==j || i+j==2)
            {
                sum+= matrix[i][j];
            }
        }
    }
    cout<<sum<<endl;
}