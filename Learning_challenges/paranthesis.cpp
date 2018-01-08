#include<iostream>
#include<string.h>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
void check (char a[], int n)
 {
   int p,q,w,i,k,x;
   q=w=0;

   for(i=0;i<n;i++)
    {
       if(a[i]==')' || a[i]=='}')
         {
           p=0;w++;
           for(x=i-1;x>=0;x--)
              {if((a[x]=='(' && a[i]==')') || (a[x]=='{' && a[i]=='}'))
                {
                   for(k=x;k<i;k++)
                    a[k]=a[k+1];
                   for(k=i-1;k<n-1;k++)
                    a[k]=a[k+2];
                   n=n-2;p=1;
                   x=-1;i=i-2;
                 }
               }
            if(p==0)
            {
             cout<<"not valid expression"<<endl;
              exit(0);
            }
          }
        else
        {
          if(a[i]=='(' || a[i]=='{')
           q++;
        }
     }

    if(q==w)
     cout<<"expression is valid in terms of paranthesis"<<endl;
    else
     cout<<"invalid expression"<<endl;
 }

main()
{
  int l;
  char a[100];
  cout<<"enter the expression "<<endl;
  gets(a);
  l=strlen(a);
  check(a,l);
}
