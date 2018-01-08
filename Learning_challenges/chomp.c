#include<stdio.h>
void main()
{
  int n,m;
  printf("enter the rows and column of choclate\n");
  scanf("%d%d",&n,&m);
  int a[n][m],i,j,x,y,t=1,q=1,k=1,s=1;

  printf("  ");
  for(j=0;j<m;j++)
  printf("%d ",j+1);
  printf("\n");

  for(i=0;i<n;i++)
  {
   printf("%d ",i+1);
   for(j=0;j<m;j++)
   {
     a[i][j]=1;
      printf("@ ");
    }
    printf("\n");
  }

  while(t==1)
  {
    k=1;
    
     while(q==1)
       {
         if(k%2==1 && s==1)
           printf("player-1 enter the coordinate as first y coordinate and second x coordinate\n");
         else
           printf("player-2 enter the coordinate as first y coordinate and second x coordinate\n");

         scanf("%d",&x);
         scanf("%d",&y);
         if(s==0)
          {
            s=1;
            k--;
          }
         
 
         if(a[x-1][y-1]!=1)
           {
             printf("wrong coordinate please reenter the coordinate\n");
             if(k%2==0)
              {
                s=0;
                break;
              }

             else
               break;
           }
          else
           {
             for(i=x-1;i>=0;i--)
             for(j=y-1;j<m;j++)
              a[i][j]=0;
             if(a[n-2][0]==1 || a[n-1][1]==1)
              {
                printf("  ");
                for(j=0;j<m;j++)
                 printf("%d ",j+1);
                printf("\n");
                for(i=0;i<n;i++)
                 {
                    printf("%d ",i+1);
                   for(j=0;j<m;j++)
                    {
                      if(a[i][j]==1)
                       printf("@ ");
                    }
                    printf("\n");
                 }
               }

             else
              {
                 if(k%2==0)
                 {
                   printf("player-2 won\n");
                   q=0;t=0;
                  }

                 else
                  {
                    printf("player-1 won\n");
                     q=0;t=0;
                  }
           
               }
           }
         k++;
        }

     }
}






