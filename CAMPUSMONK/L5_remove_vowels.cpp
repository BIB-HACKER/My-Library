#include<bits/stdc++.h>
using namespace std;
int main()
{
    string s = "Bibhakr", emp="";
    for(int i=0;i<s.size();i++)
    {
       if(s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u'|| s[i]=='a'||s[i]=='A'||s[i]=='E'||s[i]=='I'||s[i]=='O'||s[i]=='U')
       {

       }
       else{
        emp+=s[i];
       } 
    }
    cout<<emp;
}