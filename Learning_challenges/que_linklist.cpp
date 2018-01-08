#include<iostream>
#include<stdlib.h>
using namespace std;
class node
{
  int a;
  public:
  node* next;
  void input(int x)
   {
     a=x;
   }
  void output()
   {
     cout<<a<<endl;
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
      {cout<<"deleted element is ";
       f=f->next;
       f->output();
      }
   }
  void display()
   {
     if(f==r)
       cout<<"queue is empty"<<endl;
     else
      {node* t;
       for(t=f->next;t!=NULL;t=t->next)
       t->output();
      }
   }
}s;
main()
{
  int i,x;
   cout<<"enter 1 to enqueue element"<<endl;
   cout<<"enter 2 to dequeue element"<<endl;
   cout<<"enter 3 to display element of queue"<<endl;
   cout<<"enter 0 to exit the programme"<<endl;
   cin>>i;
  while(i)
   {
     switch(i)
    
    {
     case 1:  cout<<"enter the element"<<endl;
              cin>>x;
              s.enque(x);
              break;
     case 2:  s.deque();
              break;
     case 3:  s.display();
              break;
     case 0:  exit(0);
              break;
     default: cout<<"wrong entry please try aganin"<<endl;
              break;
    }
    cin>>i;
   }
}

