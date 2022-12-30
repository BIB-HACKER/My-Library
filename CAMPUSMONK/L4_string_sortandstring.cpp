#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
int main()
{
    // int
    // data_type variable_name;
    string s ="";
    // input
    cin>>s;
    string original=s;
    // sort, reverse
    // sort(s.begin(), s.end());
    reverse(s.begin(), s.end());
    // cout<<s;
    if(original==s)
    {
        cout<<"palidrome";
    }
    else
    {
        cout<<"not palindrome";
    }   
}


 