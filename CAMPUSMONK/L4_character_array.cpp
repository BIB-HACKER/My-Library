#include<iostream>
using namespace std;
int main()
{
    // char arr[10];
    // cin>>arr;
    // cout<<arr<<endl;
    string s="";

    // cin>>s;
    getline(cin, s);

    // cout<<s;
    cout<<"string size is-> "<<s.size()<<endl;

    for(int i=0;s[i]!='\0';i++)
    // {
    //     cout<<s[i]<<" ";
    // }
    if(s[i]==' ')
    {
        cout<<"contains space";
        return 0;
    }
    cout<<"does't contains space";
}