#include<iostream>
using namespace std;
/*
Inheritance :-

studet-->test
studet-->sports
test & sports --> result
*/

// ********************************* VIRTUAL BASE INHERITANCE *******************************

class student{
    protected:
    int roll_no;
    public:
    void set_number(int a)
    {
        roll_no = a;
    }
    void print_number(void)
    {
        cout << " your roll_no is "<< roll_no<<endl;
    }
};

class test : virtual public student{
    protected:
    float maths, physics;
    public:
      void set_marks(float m1, float m2)
      {
          maths = m1;
          physics = m2;
      }

      void print_marks(void){
          cout << " your result is here: "<<endl
               << " maths: "<< maths << endl
               << " physics: "<< physics << endl;
      }
};

class sports : virtual public student{
    protected:
    float score;
    public:
      void set_score(float sc)
      {
          score = sc;
      }

      void print_score(void){
          cout << " your cricket score is: " << score << endl;
      }
};

class result : public test, public sports{
    private:
    float total;
    public:
    void display(void){
        total = maths + physics + score;
        print_number();
        print_marks();
        print_score();
        cout << " your total score is: "<< total<<endl;
    }
};

int main(){
    result papon;
    papon.set_number(50);
    papon.set_marks(415, 362);
    papon.set_score(10);
    papon.display();
    return 0;
}