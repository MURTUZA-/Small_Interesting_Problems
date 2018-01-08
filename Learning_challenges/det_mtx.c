#include<stdio.h>
int det (int n,int a[n][n],int q)
{
  if(n>2)
   {
     int i,j,b[n-1][n-1],s=0;
      
         
       for(i=1;i<n;i++)
       for(j=0;j<q;j++)
         b[i-1][j]=a[i][j];

        for(i=1;i<n;i++)
       for(j=q+1;j<n;j++)
         b[i-1][j-1]=a[i][j];
         
       if(n-1!=2)
        {
          for(i=0;i<n-1;i++)
           s=s+det(n-1,b,i);
           s=s*a[0][q];
           if(q%2==0)
           return(s);
           else
            return(-s);
         }
       else
         {
           for(i=0;i<n-1;i++)
           s=s+det(n-1,b,i);
           s=s/2;
           s=s*a[0][q];
           if(q%2==0)
           return(s);
           else
           return(-s);
         }
    }
   else
      {
        int j;
        j=(a[0][0]*a[1][1])-(a[0][1]*a[1][0]);
        return(j);
       }
  }
  
 void main()
  {
	printf("enter the order of matrix\n");
	int n;
	scanf("%d",&n);
	int a[n][n],i,j,c[n];
	printf("enter the element of matrix row as major order\n");
	for(i=0;i<n;i++)
	{
	  for(j=0;j<n;j++)
	    scanf("%d",&a[i][j]);
	   printf("enter the element of next row\n");
	}
	if(n>2)
         {
          for(i=0;i<n;i++)
           
	         c[i]=det(n,a,i);
	           
	       
	        i=0;
	      for(j=0;j<n;j++)
	         i=i+c[j];
	  
           printf("determinant of given matrix is   %d\n",i);
         }
          else
           { i=det(n,a,0);
             printf("determinant of given matrix is   %d\n",i);
           }
   }
