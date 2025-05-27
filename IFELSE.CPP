#include<iostream.h>
#include<conio.h>

int a,b,c;

void main()
{
cout<<"enter 3 numbers please; " ;
cin>>a>>b>>c;
if(a<b)
	{
		if(a<c){
		cout<<a<<" is the smallest number" ;}
		else{
		if(b<c) {
				cout<<b<<" is min" ; }
		}
	}
else{
	cout<<c<<" is min";
    }
getch();
}