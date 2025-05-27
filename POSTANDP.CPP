#include <iostream.h>
#include <conio.h>
int num1= 5;
int num2 = 6 ;
int product;
int product2;
void main()
{
product = (++num1)*(++num2);
product2= (num1++)*(num2++);
cout<<"the prefix incremental product is : " << product<<endl;
cout<<"the postfix incremental product is: " <<product2<<endl;
getch();
}