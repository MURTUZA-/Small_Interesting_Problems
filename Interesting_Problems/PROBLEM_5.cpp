#include<iostream>
#include<stdlib.h>
#include<fstream>
using namespace std;

int main()
{
  int n,m,i,j,count_coloumn,count_row,l,k;
  cout<<"enter the row then coloumn "<<endl;
  cin>>n>>m;
  char c,a[n][m];

  fstream f("test");
  count_coloumn=0;
  count_row=0;

  for(i=0;i<n;i++)
  {
   for(j=0;j<m;j++)
     a[i][j]=f.get();
   c=f.get();
  }
  f.close();

 cout<<a;
/* for(i=0;i<n;i++)
 {for(j=0;j<m;j++)
  cout<<a[i][j];
 cout<<endl;
  }*/
  for(i=0;i<n;i++)
  {
   
   for(j=0;j<m;j++)
   {
     count_coloumn=0;
     count_row=0;
     if(a[i][j]!='.')
      { c=a[i][j];
        
        for(k=i;k<n && a[k][j]!='.';k++)
         count_row++;
        for(;a[i][j]!='.';j++)
         count_coloumn++;
        cout<<"tile - "<<c<<"    at ("<<j-count_coloumn<<","<<i+1<<")     "<<count_row<<"X"<<count_coloumn<<endl;
      }

     for(l=j-1;count_coloumn>0;count_coloumn--,l--)
        for(k=i;count_row>0;count_row--,k++)
         a[k][l]='.';
    }
   }

}

