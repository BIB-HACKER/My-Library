#include<iostream>
using namespace std;

int digit_sum(int num){

    int sum=0;
    while(num!=0){
        int last_digit=num%10;
        sum+=last_digit;
        num=num/10;
    }
    return sum;
}

int main()
{
    cout<<digit_sum(1257);
}
///////////////////////////////////////////////////////////////////////////////////////
// digit_sum(num):
//     int sum=0
//     while(num!=0):
//         int last_digit=num%10
//         sum+=last_digit
//         num=num/10
    
//     return sum


// print(digit_sum(1257))
