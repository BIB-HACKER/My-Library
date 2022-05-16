#include <iostream>
using namespace std;
//**************************static data member & method in c++******************************
class employee
{
    int id;
    static int count;

public:
    void setdata(void)
    {
        cout << " enter the id " << endl;
        cin >> id;
        count++;
    }
    void getdata(void)
    {
        cout << " the id of this employee " << id << " and this is employee number " << count << endl;
    }
    static void getcount(void)
    {
        cout << " the value of count is " << count << endl;
    }
};
int employee ::count = 100;

int main()
{
    employee bibhakar, paul, papon;

    bibhakar.setdata();
    bibhakar.getdata();
    employee::getcount();

    paul.setdata();
    paul.getdata();
    employee::getcount();

    papon.setdata();
    papon.getdata();
    employee::getcount();

    return 0;
}