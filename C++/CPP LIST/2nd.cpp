#include <iostream>
using namespace std;

int main()
{

    int num1;
    int num2;

    cout << "enter the denger num1:\n "; /* '<<' is called insertion operator */
    cin >> num1;                         /* '>>' this is called extraction */
    cout << "enter the denger num2:\n "; /* '<<' is called insertion operator */
    cin >> num2;
    /* this is call extraction operator*/

    cout << " the bad number is " << num1 * num2;

    return 0;
}
