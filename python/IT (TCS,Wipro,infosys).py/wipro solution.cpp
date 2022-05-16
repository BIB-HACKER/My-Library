
#include <stdio.h> 
int main()
{
     long int n;
     scanf("%ld", &n);
     int a[10]={0};
     while(n)
     {
         a[n%10]++;
         n=n/10;
     }
     int i,sk=0;
     for(i=0;i<10;i++)
     {
          if(a[i]>1)
            sk++;
     }
     if(sk==0)
        sk=-1; 
     printf("%d",sk);
}