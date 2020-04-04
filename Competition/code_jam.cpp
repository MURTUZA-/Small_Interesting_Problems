/*Standing oviation problem:- Each person in the audience have some shy level for claping, how many friends to be added to audience to make everyone clap.*/

#include<iostream>
#include <stdlib.h>
#include <fstream>
using namespace std;

long int logic(int a[],long int l)
 {
   long int count,ts;
   ts=0;count=0;
   
   long int i;
   for(i=0;i<l;i++)
    {
	  if(i<=ts)
	   ts= ts+a[i];
	  else
	   {
		 count += (i-ts);
		 ts += (i-ts);
		 ts += a[i];
	   }
	}
	return(count);
 }
    


int main()
{
	char st[15],c;
	long int x,i,j,q;
	for(i=0;i<15;i++)
	 st[i]='\0';
	
	long int T,t;
	
	fstream f("test");
	fstream f1("output.txt");
	q=1;i=0;
	while(q)
	{
	  c=f.get();
	  if(c>=48 && c<=57)
	   {st[i]=c; i++;}
	  else
	   { 
		   /*q=0;*/
		  for(j=0;j<100;j++)
		    if(c=='\n')
		     { q=0;break;}
	   }
	  
	}
	
	
    T=0;x=i-1;
    for(j=0;j<i;j++)
     {
	   
	   long int temp1;long int temp = 1;
	   for(temp1=0;temp1<x;temp1++)
	    temp =temp *10;
	   T+= (st[j]-48) * temp;
	   x--;
	 }
	 
	for(t=0;t<T;t++)
	 {
	
	   q=1;i=0;
	   while(q)
	    {
		  
		  c=f.get();
		  if(c>=48 && c<=57)
		    {st[i]=c;i++;}
		  else
		    q=0;
		}
		
	   long int frend,smax=0;x=i-1;
	   
	   for(j=0;j<i;j++)
	    {
		 
		 long int temp1;
		 long int temp = 1;
		 for(temp1=0;temp1<x;temp1++)
		  temp =temp *10;
	     smax+= (st[j]-48) * temp;
	     x--;
	    }

	    
	   int array[smax+1];
	   
	   for(i=0;i<=smax;i++)
	    { array[i]=f.get()-48;
	    }
	    c=f.get();
	    
	   /*for(i=0;i>0;i++)
	    {
	     if(f.eof() || f.get()=='\n' )
	      break;
	     }*/
	    
	     
	   frend=logic(array,smax+1);
	   char s[10],s1[10];
       long int tt,ff,j1;
       tt=t+1;
       ff=frend;
       j=0;
	   while(tt>0)
	   {
		  i=tt%10;
		  s[j]=i+48;
		  tt=tt/10;
		  j++;
	   }
	   s[j]=' ';
	   j1=0;
	   if(ff==0)
	    {s1[j1]=48;j1++;}
	   while(ff>0)
	   {
		  i=ff%10;
		  s1[j1]=i+48;
		  ff=ff/10;
		  j1++;
	   }
	   s1[j1]=' ';
	   /*cout<<s<<endl;*/
	   
	     f1<<"Case #";
      for(i=j-1;i>=0;i--)
        f1.put(s[i]);
	    f1.put(':');
	    f1.put(' ');
	  for(i=j1-1;i>=0;i--)
        f1.put(s1[i]);
	    f1.put('\n');
	    cout<<t<<"-->"<<frend<<endl;
	  }
	 f.close();
	 f1.close();
	 
 }
