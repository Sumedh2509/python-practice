#include<iostream.h>
#include<conio.h>
int m =10;  // global scope variable

void main()
{
	int m = 20 ; //local variable(in main)
	{
		int k = m ;
		int m = 30 ;  //redeclared inside a more deeper block
		cout<<"k= " <<k<<endl;
		cout<<"local m , redeclared one is "<<m<<endl;
		cout<<"the global m is " << ::m<< endl;
	}
	getch();
}