#include<stdio.h>
void main()
{
	int n,m;
	printf("enter the number of vertex in the graph\n");
	scanf("%d",&n);
	printf("enter the number of total edges present in your graph\n");
	scanf("%d",&m);
	int a[n][n],b[n],c[m+4],i,j,k,s,p,q=0;
	for(i=0;i<m+4;i++)
	 c[i]=0;
	
	printf("enter the adjecency matrix row as major order\n");
	for(i=0;i<n;i++)
	 for(j=0;j<n;j++)
	 scanf("%d",&a[i][j]);
	 
	 printf("entered matrix is\n");
	 for(i=0;i<n;i++)
	 {
	  for(j=0;j<n;j++)
	  printf("%d ",a[i][j]);
	  printf("\n");
	 }
	 printf("enter the vetices in the same order as used in the adjecency matrix\n");
	 for(i=0;i<n;i++)
	  scanf("%d",&b[i]);
	  
	 for(k=0;k<n;k++)
	 {
		 p=0;
		 s=0;
		 for(j=k;j<n;j++)
		  {
			  for(i=0;i<n;i++)
			    {
					if(a[i][j]==1)
					 {
						 c[s]=b[j];
						 s++;
						 a[i][j]=0;
						 a[j][i]=0;
						 j=i-1;
						 i=n;
					  }
					 else
					    {
							if(i==n-1)
							  p=1;
					     }
				  }
			  if(p==1)
			   {
				  if(j==k)
				   {
					   for(i=0;i<n;i++)
					    for(j=0;j<n;j++)
					      {
							if(a[i][j]==1)
					        q=1;
	                      }
	               }
	              else
	                q=1;
	                
	              j=n;
	            }
         }
        if(k==n-1 && q==1)
          { 
			  printf("no Euler circuit exist for the given graph\n");
		  }
        if(q==0)
         {
			 printf("Euler circuit is\n");
			  for(i=0;i<s;i++)
			   printf("%d\n",c[i]);
			   printf("%d\n",b[k]);
			   k=n;
		  }
	 }	 
}
