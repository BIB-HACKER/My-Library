#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
int count_vowels(string s)
{
    int cnt=0;
    for(int i=0;s.size();i++)
    {
        if(s[i]=='a' || s[i]=='e' || s[i]=='i'|| s[i]=='o'|| s[i]=='u'|| s[i]=='A'|| s[i]=='E'|| s[i]=='I'|| s[i]=='O' || s[i]=='U')
        {
            cnt+=1;
        }
    }
    return cnt;
}
int main()
{
    string s;  cin>>s;
    getline(cin, s);
    cout<<count_vowels(s);
}