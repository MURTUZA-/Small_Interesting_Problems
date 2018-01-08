#include<iostream>
#include<string.h>
#include<stdlib.h>
using namespace std;
struct names
{
  char name[20];
}s[10];

void bin(struct s[],char a[])
{ int l,h,n,q=0;
  l=0; h=9;
   while(l!=h-1)
  {
    q=0;
    n=(l+h)/2;
    if(!(strcmp(s[n],a)))
     {
       cout<<"element is present in the list at "<<n+1<<"th position"<<endl;
       q=1;
       break;
     }
    else
     {
       if((strcmp(s[n],a))>0)
        h=n;
       else
        l=n;
     }
   }
  if(q==0)
  {
    if((strcmp(s[h],a))==0)
     cout<<"element is present at "<<h+1<<"th position"<<endl;
    else
     cout<<"element is not found"<<endl;
  }
}


main()
{
   int i,j,k,q=0;
   char a[20];
   cout<<"enter 10 names to be sorted"<<endl;
   for(i=0;i<10;i++)
    cin>>s[i].name;

   for(i=0;i<10;i++)
    {
      for(j=0;j<9;j++)
       { 
          /*for(k=0;s[j].name[k]!=NULL && s[j+1].name[k]!=NULL;k++)
           {
            if(s[j].name[k]>s[j+1].name[k])
            { q=1;break;}
            if(s[j].name[k]<s[j+1].name[k])
             {q=0;break;}
           }
          if(q==1)*/
          if(strcmp(s[j].name,s[j+1].name)>0)
           {
             strcpy(a,s[j].name);
             strcpy(s[j].name,s[j+1].name);
             strcpy(s[j+1].name,a);
            }
       }
     }
    cout<<"sorted list is"<<endl;
    for(i=0;i<10;i++)
     cout<<s[i].name<<endl;

  cout<<"enter the name to be searched"<<endl;
  cin>>a;

  bin(s,a);

}
