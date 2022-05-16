#include <iostream>
#include <math.h>
using namespace std;

/*class point
{
    int a, b; //"a and b" is a values, though conduct a "p name varible".

public:
    point(int x, int y) // this point is a constructor (class "point same name point" constructor).

    {
        a = x;
        b = y;
    }
    void displaypoint()
    {
        cout << " the point is (" << a << " , " << b << ")" << endl;
    }
};

int main()
{
    (/*object) point  (/*and P is variable name) p(1, 1);
    p.displaypoint();

    point q(30, 20);
    q.displaypoint();

    point o(30, 2);
    o.displaypoint();

    point l(3, 20);
    l.displaypoint();
    return 0;
}*/

class point{
    int x;
    int y;
    public:
       friend void different(point, point);  // this line used a friend function

       point(int a, int b){
           x = a;
           y = b;
       }
       void displaypoint(){
           cout<<" the point is -> ("<<x<<" , "<<y<<")"<<endl;
       }
};
void different(point o1, point o2){
    int x_bat= o2.x - o1.x;
    int y_bat= o2.y - o1.y;
    double ball = sqrt((x_bat)*(x_bat) + (y_bat)*(y_bat));  //sqrt meanms -> (ball without sqrt value "/" by 4 bat loads)
    //   x = o1.x + o2.x;
    //   y = o1.y + o2.y;
    cout<<" distance is :-> "<<ball<<" units "<<endl;
}
int main(){
    point p1(2, 3), p2(4, 5);
    p1.displaypoint();
    p2.displaypoint();
    different(p1, p2);

}
