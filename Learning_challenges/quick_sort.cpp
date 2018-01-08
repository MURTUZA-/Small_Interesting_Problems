#include<iostream>
using namespace std;

void quick_sort(int A[],int i,int j)
 {
	int a[j-i+1],k=i+1,l=j,q=0;
	for(;k<=j;k++)
	 {
		if(A[k]<=A[i])
		 {
		   a[q]=A[k];
		   q++;
		 }
		else
		 {
			a[l-i]=A[k];
			l--;
		 }
	  }
	 a[q]=A[i];
	 for(k=0,l=i;l<=j;l++,k++)
	   A[l]=a[k];
	 if(j-i>=3)
	  {
		  quick_sort(A,i,q+i-1);
		  quick_sort(A,q+i+1,j);
	  }
 }
 
int main()
 {
	int n;
	cout<<"enter the number of elements"<<endl;
	cin>>n;
	int A[n],i;
	cout<<"enter "<<n<<" integer values"<<endl;
	for(i=0;i<n;i++)
	 cin>>A[i];
	quick_sort(A,0,n-1);
	cout<<"sorted list is ----"<<endl;
	for(i=0;i<n;i++)
	 cout<<A[i];
 }
