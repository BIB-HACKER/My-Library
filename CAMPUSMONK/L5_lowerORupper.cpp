// #include<iostream>
// #include<algorithm>
// #include<string>
// #include<cctype>
#include<bits/stdc++.h>
using namespace std;
int main()
{
    // lower upper case
    // string a = "abc";
    // string b = "ABC";
    // cout<<int('A');
    // if (a==b)
    //      cout<<"yes";
    string a= "Bibhakar";
    for(int i=0;i<a.size();i++)
    {
        // if(a[i]>='a' && a[i]<='z')
        // {
        //     a[i]-=32;
        // }
        //
        // a[i] = tolower(a[i]);  // BIG TO SMALL CONVERTER
        a[i] = toupper(a[i]);  // SMALL TO BIG CONVERTER
    }
    cout<<a<<endl;
}