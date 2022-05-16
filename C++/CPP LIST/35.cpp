#include <iostream>
using namespace std;
// ********************************** MULTILAVEL INHERITANCE DEEP DIVE ********************************

class student
{
protected:
    int roll_number;

public:
    void set_roll_number(int);
    void get_roll_number(void);
};

void student ::set_roll_number(int r)
{
    roll_number = r;
}

void student ::get_roll_number()
{
    cout << " Your roll number is : " << roll_number << endl;
}

class exam : public student
{
protected:
    float maths;
    float physics;

public:
    void set_marks(float, float);
    void get_marks(void);
};

void exam ::set_marks(float m1, float m2)
{
    maths = m1;
    physics = m2;
}

void exam ::get_marks()
{
    cout << " The marks obtained in maths are : " << maths << endl;
    cout << " The marks obtained in physics are : " << physics << endl;
}

class result : public exam
{
    float percentage;

public:
    void display_results()
    {
        get_roll_number();
        get_marks();
        cout << " Your result is " << (maths + physics) / 2 << " %" << endl;
    }
};

int main()
{
    /*
    NOTES:
    If we are inheritance B from A and C from B : [ A-->B-->C ]
    1. A is the base class from B and B is the base class from C
    2. A-->B-->C is called Inheritance Path
    */
   
  result harry;
  harry.set_roll_number(50);
  harry.set_marks(92 , 89);
  harry.display_results();
    return 0;
}  