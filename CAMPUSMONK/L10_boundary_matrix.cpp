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
    int boundary_sum=0;
    for(int i=0;i<row;i++)
    {
        for(int j=0;j<col;j++)
        {
            if(i==0 || i==row-1 || j==0 || j==col-1)
            {
                boundary_sum+= matrix[i][j];
            }
        }
    }
    cout<<boundary_sum<<endl;
}