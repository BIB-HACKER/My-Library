#include <iostream>
#include <string>
using namespace std;

//************************oops recap & Nesting of member function**************************8
class binary
{
    //private:
    string s;

public:
    void read(void); /*write your binary number*/             //all are function
    void chk_bin /*chake the binary number*/ (void);          //all are function
    void ones_compliment /*change the binary number*/ (void); //all are function
    void display /*show the all binary number*/ (void);       //all are function
};

void binary ::read(void) // this is a functiuon conplement
{
    cout << " enter a binary number " << endl;
    cin >> s;
}

void binary ::chk_bin(void) // this is a functiuon conplement
{
    for (int i = 0; i < s.length(); i++)
    {
        if (s.at(i) != '0' && s.at(i) != '1')
        {
            cout << " incorret binary format " << endl;
            exit(0);
        }
    }
}

void binary ::ones_compliment(void) // this is a functiuon conplement
{
    for (int i = 0; i < s.length(); i++)
    {
        if (s.at(i) == '0')
        {
            s.at(i) = '1';
        }
        else
        {
            s.at(i) = '0';
        }
    }
}

void binary ::display(void) // this is a functiuon conplement
{
    cout << " display your binary number " << endl;
    for (int i = 0; i < s.length(); i++)
    {
        cout << s.at(i);
    }
    cout << endl;
}

int main()
{
    binary b; // b is a object
    b.read();
    b.chk_bin();
    b.ones_compliment();
    b.display();

    return 0;
}