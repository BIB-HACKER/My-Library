#include <iostream>
using namespace std;

int main()
{

    int marks[4] = {23, 34, 56, 78};   

    int mathmaks[4];
    mathmaks[0] = 123;
    mathmaks[1] = 223;
    mathmaks[2] = 323;
    mathmaks[3] = 423;

    cout << "the mathmarks is " << endl;
    cout << mathmaks[0] << endl;
    cout << mathmaks[1] << endl;
    mathmaks[2] = 777; //you can change the value of array
    cout << mathmaks[2] << endl;
    cout << mathmaks[3] << endl;

    cout << " the students marks is  " << endl;
    cout << marks[0] << endl;
    cout << marks[1] << endl;
    cout << marks[2] << endl;
    cout << marks[3] << endl;

                                                    //**************************project(for loop)

    // for (int i = 0; i < 4; i++)
    // {
    //     cout << "the marks of good students "<<i<< " is " <<marks[i]<<endl;

    // }
                                                 //******************************project(while loop)

    // int i = 0;
    // int marks[] = {12, 23, 34, 45, 67, 78, 90, 56, 35, 88};

    //  cout<<" using while loop :- "<<endl;
    //  while (i<10)

    //  {
    //     cout<< " the value of marks is "<<i<< " is " <<marks[i]<<endl;
    //     i++;
    //  }

                                                          //**********************PROJECT(do-while)

    // cout << " using do-while loop " << endl;
    // do
    // {
    //     cout << " the marks of student:- " << i << " is " << marks[i] << endl;
    //     i++;
    // } while (i<8);

        //**************************pointer arithmetic and arrays*********************

        int* p = marks;
        cout<<"the ponter of arrays "<<endl;
        cout<<*(p)<<endl;
        cout<<*(p+1)<<endl;
        cout<<*(p+2)<<endl;  
        cout<<*(p+3)<<endl;  
        // cout<< " the value of marks[0] is "<<*p<<endl;                   
        // cout<< " the value of marks[0] is "<<*(p+1)<<endl;                   
        // cout<< " the value of marks[0] is "<<*(p+2)<<endl;                   
        // cout<< " the value of marks[0] is "<<*(p+3)<<endl;                   
    return 0;
}