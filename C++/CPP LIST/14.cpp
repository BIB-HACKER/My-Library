#include <iostream>
using namespace std;

inline int product(int a, int b)       
//                                    ******************static vareable**************************
{
    // when inline function use then static vateable not used******
    // static int c = 0; //tis exicute only one time and save value next and next time
    // c = c + 1;
    return a * b; //+c;
}

                                       //*****************defailt argument**************************
                                         
float moneyrecived(int money, float factor=1.04){
         return money*factor;
}

// int strlen(const char *money)   {

// }                                            //constant argument value on coding

int main()
{
    // int a, b;
    // cout << " the valiue of a and b " << endl;
    // cin >> a >> b;
    // cout << " the product of a and b is " << product(a, b) << endl;
    // cout << " the product of a and b is " << product(a, b) << endl;
    // coutyouthe product of a and b is " << product(a, b) << endl;
 
 int money = 15000;
 cout<<" you have "<<money<<" RS your bank acount, you will recived "<<moneyrecived(money)<<" RS after 1 year "<<endl;
 cout<<" for VIP "<<money<<" RS your bank acount, you will recived "<<moneyrecived(money, 1.10)<<" RS after 1 year ";


    return 0;   
}