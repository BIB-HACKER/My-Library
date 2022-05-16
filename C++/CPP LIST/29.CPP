#include<iostream>
using namespace std;

//*****************************************dynamic initialization of object using constructors**************************************
class bankdeposit{
    int principle ;
    int years;
    int interestrate;
    int returnvalue;

    public:
    bankdeposit(){}
    bankdeposit(int p, int y, float r);
    bankdeposit(int p, int y, int R);
    void show ();
};

bankdeposit :: bankdeposit(int p, int y, float r)  //this is a constructor**********************************
{
    principle = p;
    years = y;
    interestrate = r;
    returnvalue = principle;
    for (int i = 0; i < y; i++)
    {
         returnvalue = returnvalue*(1+interestrate);
    }
}

bankdeposit :: bankdeposit(int p, int y, int R)     //this is a constructor**********************************
{
    principle = p;
    years = y;
    interestrate = float(R)/100;
    returnvalue = principle;
    for (int i = 0; i < y; i++)
    {
         returnvalue = returnvalue*(1+interestrate);
    }
}

void bankdeposit :: show(){        //this is a function**********************************
     cout<<endl<<" principle amount was "<<principle<<" return value after "<<years<< " years is "<<returnvalue<<endl;
}

int main(){
    bankdeposit /* this is a bankdeposite OBJECT (bd1, bd2, bd3) */ bd1, bd2, bd3;
    int p,y;
    float r;
    int R;

    cout << " enter the value of p y and r "<<endl;  //object
    cin>>p>>y>>r;
    bd1 = bankdeposit(p, y, r);
    bd1.show();

    cout << " enter the value of p y and R "<<endl;   //object
    cin>>p>>y>>R;
    bd2 = bankdeposit(p, y, R);
    bd2.show();
    
    return 0;
}      