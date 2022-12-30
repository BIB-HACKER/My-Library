#include<iostream>
using namespace std;
int main()
{
    // find first index of element x in array
    // if not present then print -1;
    int n; cin>>n;
    int arr[n];
    for(int i=0;i<n;i++)
    {
        cin>>arr[i]
    }

    int x; cin>>x;
    for(int i=0;i<n;i++)
    {
        if(arr[i]==x)
        {
            cout<<i<<endl;
            return 0;
        }
    }
    cout<<-1<<endl;
}

///////////////////////////////////////////////////

#include<iostream>
using namespace std;
int main()
{
    // find last index of element x in array
    // if not present then print -1;
    int n; cin>>n;
    int arr[n];
    for(int i=0;i<n;i++)
    {
        cin>>arr[i]
    }

    int x; cin>>x;
    for(int i=;i<n;i++)
    {
        if(arr[i]==x)
        {
            cout<<i<<endl;
            return 0;
        }
    }
    cout<<-1<<endl;
}
///////////////////////////////////////////

#include<iostream>
using namespace std;
int main()
{
    // find last index of element x in array
    // if not present then print -1;
    int n; cin>>n;
    int arr[n];
    for(int i=0;i<n;i++)
    {
        cin>>arr[i]
    }

    int x; cin>>x;
    int index=-1;
    for(int i=;i<n;i++)
    {
        if(arr[i]==x)
        {
            index=i;
            break;
        }
    }
    cout<<break<<endl;
}