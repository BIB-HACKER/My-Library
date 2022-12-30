#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    string one, two; cin>>one>>two;
    // given two string check if they are rotaion of each or not?
    string check = one + one;    // abcabc  == bac
    auto index = check.find(two);
    cout<<index<<endl;
    if(index != string::npos)
    {
        cout<<"yes, they are rotation of each other"<<endl;
    }
    else{
        cout<<"no, they are not"<<endl; 
    }
}