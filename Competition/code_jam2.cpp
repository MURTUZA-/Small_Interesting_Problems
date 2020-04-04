
#include<iostream>
#include<fstream>
#include<stdlib.h>
using namespace std;
class node
{
 public:
  int a;

  node* next;
  void input(int x)
   {
     a=x;
   }
  int data()
   {
     return(a);
   }
};

class que
{
  public:
   node *f;
   node *r;
  que()
   {
     r=new node;
     f=r;
   }

  void enque(int x)
   {
     node* t;
      t=new node;
     if(t==NULL)
       cout<<"memory is full"<<endl;
     else
      {
       t->input(x);
       
       t->next=NULL;
       r->next=t;
       cout<<"element is enqueued"<<endl;
       r=t;
      }
   }
 
  void deque()
   {
     if(f==r)
       cout<<"queue is empty"<<endl;
     else
      {node*t;
	    while(f!=r)
         {
			 t=f;
			 f=f->next;
			 delete(t);
		 }
      }
    }
   
   
  node* maximum1()
   {
	  node *t,*ptr_max;
	  ptr_max= NULL;
     if(f==r)
       cout<<"queue is empty"<<endl;
     else
      {
	    int max=0;
	    ptr_max=f->next;
       for(t=f->next;t!=r;t=t->next)
        {
		  if(t->data()>max)
		    {
				max=t->data();
		        ptr_max=t;
		    }
		}
		if(t->a>max)
		 ptr_max=t;
      }
      return(ptr_max);
   }

  node* minimum1()
   {
	 node* t,*ptr_min;
	 ptr_min=NULL;
     if(f==r)
       cout<<"queue is empty"<<endl;
     else
      {
	    int min=(f->next)->a;
	    ptr_min=f->next;
       for(t=f->next;t!=r;t=t->next)
        {
		  if(t->data()<min)
		    {
				min=t->data();
		        ptr_min=t;
		    }
		}
		if(t->a<min)
		 ptr_min=t;
      }
     return(ptr_min);
   }


}A,B;

void divide_insert(node*p)
 {
   node*t;
   t=new node;
   t->a=p->a/2;
   p->a=p->a - t->a;
   t->next=p->next;
   p->next=t;
 }

void distribute(int count,node* max)
 {
   if(max->a>1)
    {
	  divide_insert(max);
	   max=A.maximum1();
	   B.enque(max->a+count);
	   distribute(count+1,max);
	 }
  }


int main()
 {
   	char st[50],c;
	long int x,i,j,q;
	long int T,t;
	
	fstream f("test2");
	fstream f1("output2.txt");
	q=1;i=0;
	while(q)
	{
	  c=f.get();
	  if(c>=48 && c<=57)
	   {st[i]=c; i++;}
	  else
	   { 
		  for(j=0;j<100;j++)
		    if(c=='\n')
		     { q=0;break;}
	   } 
	}
	cout<<"test cases  = "<<st<<endl;
	
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
		
	   int D=0;x=i-1;
	   
	   for(j=0;j<i;j++)
	    {
		 long int temp1;
		 long int temp = 1;
		 for(temp1=0;temp1<x;temp1++)
		  temp =temp *10;
	      D+= (st[j]-48) * temp;
	     x--;
	    }
       cout<<"value of D  "<<D<<endl;
	   /*int array[D];*/
	   
	   cout<<"array of case "<<t+1<<"   "<<endl;
	   
	   for(i=0;i<D;i++)
	     {
		   int n;
		   q=1;n=0;
	       while(q)
	       {
		     c=f.get();
		     if(c>=48 && c<=57)
		      {st[n]=c;n++;}
		     else
		      q=0;
		    }
		    x=n-1;
	        q=0;
	       for(j=0;j<n;j++)
	       {
		    int temp1;
		    int temp = 1;
		    for(temp1=0;temp1<x;temp1++)
		     temp =temp *10;
	         q+= (st[j]-48) * temp;
	         x--;
	        }
            cout<<q<<" ";
           A.enque(q);
	       /*c=f.get();*/
	     }
	     cout<<endl;
	   
	   node*l;
	   l=A.maximum1();
	   B.enque(l->a);
	   
	   distribute(1,A.maximum1());
       
       int runing_op;
       
       l=B.minimum1();	   
	   runing_op=l->a;
	   
	   
	   f1<<"Case #";
	   char s[10],s1[10];
	   int tt,ff,j1;
	   tt=t+1;
       ff=runing_op;
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

      for(i=j-1;i>=0;i--)
        f1.put(s[i]);
	    f1.put(':');
	    f1.put(' ');
	  for(i=j1-1;i>=0;i--)
        f1.put(s1[i]);
	    f1.put('\n');
	   /* cout<<t<<"-->"<<runing_op<<endl;*/
	   for(node*k=B.f->next;k!=B.r;k=k->next)
	   cout<<k->a<<" "<<endl;

	   A.deque();
	   B.deque();
    }
    f.close();
    f1.close();
 }
