
//*********************selection structure**********************

#include <iostream>

using namespace std;

int main()
{
    //cout << " jroigjoi";

    int age;

    cout << " tell me youe age" << endl;
    cin >> age;

    //********if-else else ladder********
    // if((age<20) && (age>4)){
    //     cout<<" you cant drink "<<endl;
    // }
    // else if(age==20){
    //     cout<<" you just tuch and fell a drink "<<endl;
    // }
    // else if(age<5){
    //     cout<<" you dont tuch a drink "<<endl;
    // }
    // else if(age>=60){
    //     cout<<" your helth isshu for you can drink "<<endl;
    // }
    // else{
    //     cout<<" you can drink to my party "<<endl;

    // }

    //     ***************switch case statement**************

    switch (age)
    {
    case 18:
        cout << " you are child " << endl;
        break;
    case 20:
        cout << " you are mature " << endl;
        break;
    case 50:
        cout << " you are old " << endl;
        break;

    default:
        cout << " no people are hare " << endl;
        break;
    }

    cout<<" you are boss"; 
    return 0;
}