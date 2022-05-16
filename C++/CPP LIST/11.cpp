#include<iostream>
using namespace std;

           //**************************structures**************************

typedef struct hacker
{
    int id;
    char os;
    int salary;

}boos; //typedef->(struct hacker = boos)

// int main(){

//     boos bibhacker;
//     boos papai;
//     boos malay;
//     bibhacker.os = 'L';
//     bibhacker.id = 5;
//     bibhacker.salary = 105000000;

//     cout<<" the hacker fv os is "<<bibhacker.os<<endl;
//     cout<<" the hacker id is "<<bibhacker.id<<endl;
//     cout<<" the hacker salary is "<<bibhacker.salary<<endl;

    //        *************************unions************************

    union money
    {
        /* data */
        int price;
        char brand;
        float supply;
        int worker;
    };
         //******************//C++ union worked a better memeory mamgement on coding 

    // int main(){
        
        // union money mobile;
        // mobile.price = 10;
        // mobile.brand = 'A';
        // mobile.supply = 550;
        // mobile.worker = 559000;
        // cout<<mobile.worker;             

        //******************************enums******************************

    int main(){

    enum Meal{ breakfast, workout, protinsheek, jym, lunch, dineer};
    Meal b1 = jym;
    cout<<b1;      


    return 0;
}