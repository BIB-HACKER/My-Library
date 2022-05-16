#include<iostream>
using namespace std;

class employee{
    int id;
    int salary;

    public:
    void setid(void){
        salary = 200000;
        cout<<" enter the id of employee "<<endl;
         cin>>id;
        cout<<" salary of employe is 200000 "<<endl;
       
    }
    void getid(void){
        cout<<" the id of this employee is "<<id+5<<endl;
    }
};

int main(){
    // employee bibhakar, malay, papai;
    // bibhakar.setid();
    // bibhakar.getid();
    
    employee hack[5];
    for(int i = 1; i < 6; i++)
    {
        hack[i].setid();
        hack[i].getid();
    }
    return 0;
}