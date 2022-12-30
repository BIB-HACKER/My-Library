// #include<iostream>
// using namespace std;
// void printArrayElementns(int arr[], int n, int index)
// {
//     if (index==n)
//     {
//         return;
//     }
//     cout<<arr[index]<<;
//     printArrayElementns(arr,n, index+1);
// }
// int main()
// {
//     int n=5;
//     int arr[n] = {5,10,20,1,18}:
//     int index=0;
//     printArrayElementns(arr, n,index);
// }
####################################

#include<iostream>
using namespace std;
void printArrayElementns(int arr[], int n)
{
        if(n<=0) return;
        printArrayElementns(arr,n-1);
        cout<<arr[n-1]<<" ";
}
int main()
{
    int n=5;
    int arr[n] = {5,10,20,1,18}:
    printArrayElementns(arr, n);
}