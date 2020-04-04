#include <iostream>
using namespace std;
/*compute factorial of large no*/  
  int main()
{
  int n,f[400],counter=0,temp,i;/*array f containing factorial value */
  f[0]=1;
  cout<<"Enter the number to calculate factorial"<<endl;
  cin>>n;
  
  while(n>=2)
 {
   temp=0;
   for(i=0;i<=counter;i++) 
  {
   temp=(f[i]*n)+temp;/*temp is used for carring bits*/
   f[i]=temp%10;/*last bits are stored*/
   temp=temp/10;
  }
    while(temp>0)
   {
    f[++counter]=temp%10;/*carry bit is getting stored*/
    temp=temp/10;
   }
   n--;
 }
   for(i=counter;i>=0;i--)
   cout<<f[i];
}




