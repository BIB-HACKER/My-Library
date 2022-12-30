#include<iostream>
#include<algorithm>
#include<string>
using namespace std;
int main()
{
    string text, pattern; cin>>text>>pattern;
    bool present = false;
    int cnt=0;
    for(int i=0;i<text.size();i++)
    {
        if(pattern[0] == text[i])
        {
            int text_pointer = i;
            for(int j=0; j<pattern.size();j++)
            {
                if(pattern[j]!=text[text_pointer])
                {
                    break;
                }
                text_pointer++;
            }
            if(text_pointer == i + pattern.size())
            {
                // pattern found
                // cout<<i<<" ";
                // present=true;
                cnt++;
            }
        }
    }
    // if(present == true)
    // {
    //     cout<<"YES"<<endl;
    // }
    // else
    // {
    //     cout<<"NO"<<endl;
    // }
    cout<<cnt<<endl;
}