#include<iostream>
using namespace std;

main()
{
  int n;
  cout<<"enter the number of element"<<endl;
  cin>>n;
  int a[n],l,h,i,q=0;

  cout<<"enter sorted"<<n<<" integer"<<endl;
  for(i=0;i<n;i++)
   cin>>a[i];

  cout<<"enter the number to be searched"<<endl;
  cin>>i;

  h=n-1; l=0;
 
  while(l!=h-1)
  {
    n=(l+h)/2;
    if(a[n]==i)
     {
       cout<<"element is present in the list at "<<n+1<<"th position"<<endl;
       q=1;
       break;
     }
    else
     {
       if(a[n]>i)
        h=n;
       else
        l=n;
     }
   }
  if(q==0)
   {
      if(a[h]==i)
       cout<<"element is present at "<<h+1<<"th position"<<endl;
      else
       cout<<"element is not found"<<endl;
   }
}



