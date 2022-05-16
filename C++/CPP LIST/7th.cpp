#include <iostream>

using namespace std;

int main()
{

    //******************loops in c++*****************
    //types of loops - 1> for loop
    //  2> while loop
    //  3> do-while loop

    /*for loop************************************
      syntex for loop
      for (initialization; condition; updation)
      {
          loop body(c++ code)
      }*/


    //       for(int i= -100; i <= 80; i++)
    // {
    //     cout<<i<<endl;
    // }

    /*infiite for loop*/

    //       for(int i= -100; 79 <= 80  0; i++)
    // {
    //     cout<<i<<endl;
    // }

    /*while loop *************************************/
    //syntex:
    //while(condition):
    // {
    // c++ statements;
    //  }
    

    // int o = 1;
    // while(o <= 50){

    //     cout<<o<<endl;
    //     o++;
    // }

                                     /**********************PROLECT*/

    int k = 5;
    cout << "the multiplication table of 5 is: \n";
    int o = 1;
    while (o <= 5)
    {
        cout << k << "X" << o << "=" << k * o << endl;
        o++;
    }

    //example of infinite while loop
    // int o = 1;
    // while(true){

    //     cout<<o<<endl;
    //     o++;
    // }

    /*do-while loop*****************************************/

    // int p = 1;
    // do{
    //     cout<<p<<endl;
    //     p++;
    // }while(p>65);

                                                 /**********************PROLECT*/

    // int b = 5;
    // cout <<" multiplication table of 6 is "<<endl;
    // int l = 8;
    // do{
    //     cout<<b<<"X"<<l<<"="<<b*l<<endl;
    //     l++;

    // }while(l<20);

    return 0;
}
