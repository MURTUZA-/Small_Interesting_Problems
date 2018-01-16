#include<iostream>
using namespace std;

int main()
{
  int n,i;
  cout<<"enter the number"<<endl;
  cin>>n;
  
  while (n>1)
  {
    i=n%3;
    switch(i)
    {
      case 0: n=n/3;
              cout<<"3 ";
              break;
      case 1: n=n-1;
              cout<<"-1 ";
              break;
      case 2: if(n%2==0)
               { n=n/2; cout<<"2 ";}
              else
               { n=n-1; cout<<"-1 ";}
              break;
    }
  }
 cout<<endl;
}
                
