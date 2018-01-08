/*#include<iostream>*/
#include<stdio.h>
using namespace std;
const int n=4;
void nque (int A[n][n],int i,int j)
{
  int q,p=0;
  q=0;
  int k,l;
  if(i<n)
   {
     for(;j<n;j++)
      {
        for(k=0;k<j;k++)
         {
           if(A[i][k]==1)
            { q=1;break;}
         }

        for(k=0;k<i;k++)
          if(A[k][j]==1)
            { q=1;break;}
        
        for(k=j,l=i;k>=0 && l>=0;k--,l--)
           if(A[l][k]==1)
            { q=1;break;}
        
        for(k=j,l=i;k<n && l>=0;k++,l--)
           if(A[l][k]==1)
             { q=1;break;}
                  
        if(q==0)
         {
           A[i][j]=1;
           q=1;
           nque(A,i+1,0);
           break;
         }
        else
          q=0;
      }
     if(q!=1)
      p=1;
    }

   if(p==1)
    {
	 for(q=1;i-q>=0;q++)
      {
	   for(j=0;j<n;j++)
        if(A[i-q][j]==1)
         {
           A[i-q][j]=0;
           break;
         }
       if(j<n-1)
         {
		   nque(A,i-q,j+1);
		   break;
		 }
      /*else
        {
          for(j=0;j<n;j++)
            if(A[i-2][j]==1)
             {
               A[i-2][j]==0;
             }
          nque(A,i-2,j+1);
         }*/
       }
      if(q>i)
       printf("No possible solution\n");
     }
}

main()
{
  /*int n;*/
  /*cout<<"enter the dimension of chess board as either raw or column of"<<endl;*/
  printf("enter the dimension of chess board as either raw or column of");
  /*cin>>n;
  scanf("%d",&n);*/

  int A[n][n],i,j;
  for(i=0;i<n;i++)
   for(j=0;j<n;j++)
    A[i][j]=0;
  nque(A,0,0);

  for(i=0;i<n;i++)
  /* cout<<"_";
  cout<<endl;*/
  printf("_");
  printf("\n");
  for(i=0;i<n;i++)
   {
     /*cout<<"|";*/
     printf("|");
     for(j=0;j<n;j++)
      {
        if(A[i][j]==0)
          /*cout<<"_|";*/
          printf("_|");
        else
          /*cout<<"@|";*/
          printf("@|");
       }
      /*cout<<endl;*/
      printf("\n");
    }
   /*cout<<"here '@' representes the position of queen on the chess board"<<endl;*/
}
