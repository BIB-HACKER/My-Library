#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
int count_words(string s)
{
    int cnt=0;
    for(int i=0;s.size();i++)
    {
        if(s[i]==' ')
        {
            cnt++;
        }
    }
    return (cnt+1);
}
int main()
{
    string s;  cin>>s;
    getline(cin, s);
    cout<<count_words(s);
    //count words in a string
}