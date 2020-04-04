#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
using namespace std;
const int n=6;

struct node
 {
   char a[n];
   node *next,*pre;
 }*p,*q;

int main()
 {
   p=NULL;
   char s1[n],s2[n],s[n];
   int i=1;
   cout<<"enter prefix expression"<<endl;
   cout<<"Enter character 'a' after the last charcter of expression"<<endl;
   while(i)
    {
      cin>>s;
      if(s[0]=='a')
       i=0;
      else
      {
      if(p==NULL)
       {
         p=new node;
         q=p;
         p->next=NULL;
         p->pre=NULL;
       }
      else
       {
         node *temp;
         temp=new node;
         p->next=temp;
         temp->pre=p;
         temp->next=NULL;
         p=p->next;
       }
      strcpy(p->a,s);
      
      }    
    }

    while(p!=NULL)
     {
       
       if(!(p->a[0]>=48 && p->a[0]<=57))
         
        {
          node *temp;
          temp=p->next;
          strcpy(s1,(p->next)->a);
          strcpy(s2,((p->next)->next)->a);
          if(p->pre!=NULL)
          (((p->next)->next)->next)->pre = p;
          p->next=((p->next)->next)->next;
          delete(temp->next);
          delete(temp);
          int l1,l2,n1,n2;
        
          l1=strlen(s1);
          l2=strlen(s2);
          n1=0;
          n2=0;
 
          for(i=l1-1;i>=0;i--)
            n1=(s1[i]-48)*pow(10,l1-i-1)+n1;
  
         
          
          for(i=l2-1;i>=0;i--)
            n2=(s2[i]-48)*pow(10,l2-i-1)+n2;
          
          
          
           
             
             if(p->a[0]=='+')  
                {     l1=n1+n2;
                      for(i=0;l1>0;l1=l1/10)
                       { s1[i]=(l1%10)+48; i++;}
                  
                      
                      l2=i;
                      for(i=0;i<l2;i++)
                      p->a[i]=s1[l2-i-1];

                        
               }
             if(p->a[0]=='-')
             {  
                      l1=n1-n2;
                      for(i=0;l1>0;l1=l1/10)
                       { s1[i]=(l1%10)+48; i++;}
                      l2=i;
                      for(i=0;i<l2;i++)
                      p->a[i]=s1[l2-i-1];
                  
              } 
             if(p->a[0]=='*') 
                {      l1=n1*n2;
                      for(i=0;l1>0;l1=l1/10)
                       { s1[i]=(l1%10)+48; i++;}
                      l2=i;
                      for(i=0;i<l2;i++)
                      p->a[i]=s1[l2-i-1];
                }
                
             if(p->a[0]=='/') 
             {         l1=n1/n2;
                      for(i=0;l1>0;l1=l1/10)
                       { s1[i]=(l1%10)+48; i++;}
                      l2=i;
                      for(i=0;i<l2;i++)
                      p->a[i]=s1[l2-i-1];
              
             }  
             if(p->a[0]=='%') 
               {       l1=n1%n2;
                      for(i=0;l1>0;l1=l1/10)
                       { s1[i]=(l1%10)+48; i++;}
                      l2=i;
                      for(i=0;i<l2;i++)
                      p->a[i]=s1[l2-i-1];
                      p->a[i]=0;
              
			 }
             
         }
       
       p=p->pre;
      }
   

    cout<<q->a<<endl;
 }
