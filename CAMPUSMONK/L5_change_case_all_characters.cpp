#include<bits/stdc++.h>
using namespace std;
int main()
{
    string s="Bibhakar Paul";
    for(int i=0;i<s.size();i++)
    {
        if(s[i]>='a' && s[i]<='z')
        {
            s[i]-=32;
        }
        if(s[i]==' ')
        {
            s[i]*=1;
        }
        else
        {
            s[i]+=32;
        }
    }
    cout<<s<<endl;
}
