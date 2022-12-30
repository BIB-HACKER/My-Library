#include<iostream>
#include<string>
using namespace std;
int main()
{
    string s; cin>>s;
    string v;
    for(int i=0;i<s.size();i++)
    {
        bool repeating = false;
        for(int j=0;j<s.size();j++)
        {
            if(j != i)
            {
                if(s[j] == s[i])
                {
                    repeating=true;
                    break;
                }
            }
        }
        if(repeating==false)
        {
            v+=s[i]+" ";
        }
    }
    if(v!=" ")
    {
        cout<<s<<endl;
    }
    cout<<v<<endl;
}