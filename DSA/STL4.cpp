// STL -> standard template library
// stl is a 4 part = 1. algorithms
//                   2. containers
//                   3. function
//                   4. iterators


//pairs(utility library)
#include<bits/stdc++.h>
using namespace std;

void explainpair(){
    pair<int, int> l = {1,3};
    cout<<l.first<<" "<<l.second;
    
    pair<int, pair<int,int>> p = {1,{4,7}};
    cout<<p.first<<" "<<p.second.first<<" "<<p.second.second;
    
    pair<int, int> arr[] = {{1,2}, {4,6}, {7,9}};
    cout<<arr[2].first;

    
}
int main(){
    explainpair();
    return 0;
}