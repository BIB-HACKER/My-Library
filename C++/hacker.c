#include<stdio.h>
  main()
  {clrser();
  float num1;
  float num2;
  char op;
  float result;

printf("enter the first number;");
scanf("%d", &num1);

printf("enter the operation :");
scanf(" %d, & op");

printf("enter the second number :");
scanf("%f", &num2);

switch (op)
{
case '-':
result =num1-num2;
printf("%f", result);
    break;

    case'+':
    result =num1+num2;
    printf("%f",result);
    break;535

    case'*':
    result =num1*num2;
    printf("%f", result);
    break;

    case'/':
    result =num1+num2;
    printf("%f", result);
    break;

default:
printf("the operation is not valid :");
}
getch();

}