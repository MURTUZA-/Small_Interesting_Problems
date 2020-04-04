#include<stdio.h>
int i,j,n,heapsize;
int A[20];
void swap(int A[],int x, int y);
void heapify(int A[],int i);
void buildheap(int A[]);
int main()
{
	printf("enter no. of elements:\n");
	scanf("%d", &n);
	for(i=0;i<n;i++)
	{
		//printf("enter element[%d]:\n",i+1);
		scanf("%d", &A[i]);
	}
	buildheap(A);
	printf("the heap is:\n");
	for(i=0;i<n;i++)
	{
		printf("%d\t",A[i]);
	}
	printf("\n\n");
	heapsize=n;
	for(i=heapsize-1;i>=1;i--)
	{
		swap(A,i,0);
		n=n-1;
		heapify(A,0);
		for(i=0;i<n;i++)
		{
		printf("%d\t", A[i]);}
		printf("\n");
	}
	printf("\nthe sorted array is: \n");
	for(i=0;i<heapsize;i++)
	printf("%d\t", A[i]);
        printf("\n");
	return 0;
}
void swap(int A[],int x, int y)
{
	int temp;
	temp=A[x];
	A[x]=A[y];
	A[y]=temp;
}
void heapify(int A[],int i)
{
	int l,r;
	l=2*i+1;
	r=(i*2)+2;
	if(l<n && A[l]>A[i])
	{
		swap(A,i,l);
		heapify(A,2*i+1);
	}
	if(r<n && A[r]>A[i])
	{
		swap(A,i,r);
		heapify(A,2*i+2);
	}
}
void buildheap(int A[])
{
	for(i=n/2;i>=0;i--)
	{
		heapify(A,i);
	}
}
