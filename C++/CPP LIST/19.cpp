//********************MEMORY ALLOCATION & USING ARRAY IN class( c+clas = c++)******************************
#include <iostream>
using namespace std;

class shop
{
    int counter;
    int itemprice[800];
    int itemid[900];
    

  public :
    void incounter(void) {counter = 0; }
    void setprice(void);
    void displayprice(void);
};

void shop ::setprice(void)
{
    cout << " Eneter id of your item no " << counter + 1 << endl;
    cin >> itemid[counter];
    cout << " Enter price of your item " << endl;
    cin >> itemprice[counter];
    counter++;
}

void shop ::displayprice(void)
{
    for (int i = 0; i < counter; i++)
    {
        cout << " the price of item with id " << itemid[i] << " is " << itemprice[i] << endl;
    }
}

int main()
{

    shop dookan;
    dookan.incounter();
    dookan.setprice();
    dookan.setprice();
    dookan.setprice();
    dookan.setprice();
    dookan.displayprice();

    return 0;
}  