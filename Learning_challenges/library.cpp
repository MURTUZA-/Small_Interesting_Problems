#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
struct book
 {
	 char publisher[20],title[20];
	 int isbn,year;
	 book *left,*right;
 }*tree, *root;
 


void insert()
{
	if(tree==NULL)
	 {
		tree=new book;
		if(tree==NULL)
		  cout<<"memory full"<<endl;
		else
		  {
			 cout<<"enter isbn"<<endl;
			 cin>>tree->isbn;
			 cout<<"enter name of publisher"<<endl;
             getchar();
             gets(tree->publisher);
             getchar();
             cout<<"enter the title of book"<<endl;
             getchar();
             gets(tree->title);
             getchar();
             cout<<"enter the year of publication"<<endl;
             cin>>tree->year;
             tree->left=tree->right=NULL;
             root=tree;
          }
      }
     else
      {
		 book *temp;
		 temp=root;
		 int x,q=1;
		 tree=new book;
		 if(tree=NULL)
		   cout<<"memory full"<<endl;
		 else
		   {
			  cout<<"enter isbn"<<endl;
			  cin>>x;
			  while(q)
			   {
				   if(temp->isbn >x)
				     {
						if(temp->left!=NULL)
						  temp=temp->left;
						else
						  {
							 temp->left=tree;
							 tree->isbn=x;
							 cout<<"enter the name of publisher"<<endl;
                                                         getchar();
							 gets(tree->publisher);
                                                         getchar();
							 cout<<"enter the title of book"<<endl;
                                                         getchar();
							 gets(tree->title);
                                                         getchar();
							 cout<<"enter the year of publication"<<endl;
							 cin>>tree->year;
						     
						     tree->left=NULL;tree->right=NULL;
						     q=0;
						  }
					  }
					else
					  {
						  if(temp->right != NULL)
						    temp=temp->right;
						  else
						    {
							   temp->right=tree;
							    tree->isbn=x;
							   cout<<"enter the name of publisher"<<endl;
                                                           getchar();
							   gets(tree->publisher);
                                                           getchar();
							   cout<<"enter the title of book"<<endl;
                                                           getchar();
							   gets(tree->title);
                                                           getchar();
							   cout<<"enter the year of publication"<<endl;
							   cin>>tree->year;
						     
						       tree->left=NULL;tree->right=NULL;
						       q=0;
						    }
						}
				 }
			}
		}
 }
 
 struct book* search(int x)
   {
	  tree=root;
	  if(tree==NULL)
	    {
              cout<<"database is empty"<<endl;
              return(NULL);
            }
	  else
	    {
		   int q=1;
		   while(q)
		    {
			   if(tree->isbn==x)
			     {
					cout<<"book is found"<<endl;
					q=0;
                                        return(tree);
				 }
			   else
			     {
					if(tree->isbn > x)
					  {
						 if(tree->left==NULL)
						   {
							  cout<<"not found"<<endl;
							  q=0;return(NULL);
						   }
						 else
						   tree=tree->left;
					  }
					else
				      {
						 if(tree->left==NULL)
						   {
							  cout<<"not found"<<endl;
							  q=0;return(NULL);
						   }
						 else
						   tree=tree->right;
					  }
				 }
			}
		}
	}


void delett(int x)
 {
   tree=search(x);
   if(tree!=NULL)
    {
      book *temp;
      temp=tree;
      if(tree->right != NULL)
       {
         tree=tree->right;
         int flag=1;
         while(flag)
          {
             if(tree->left==NULL)
              {
                swap(tree,temp);
                if(tree->right!=NULL)
                  {
                    temp->right=tree->right;
                    delete(tree);
                  }
                else
                  {
                    temp->right=NULL;
                    delete(tree);
                    flag=0;
                  }
              }
             else
              {
                 if((tree->left)->left==NULL)
                  {
                    swap(temp,tree->left);
                    if((tree->left)->right!=NULL)
                     {
                       temp=tree->left;
                       tree->left=(tree->left)->right;
                       delete(temp);
                       flag=0;
                     }
                    else
                     {
                       delete(tree->left);
                       tree->left=NULL;
                       flag=0;
                     }
                  }
                 else
                   tree=tree->left;
             }
          }
    }
   else
    {
      if(tree->left!=NULL)
       {
          tree=tree->left;
          int flag=1;
         while(flag)
          {
             if(tree->right==NULL)
              {
                swap(tree,temp);
                if(tree->left!=NULL)
                  {
                    temp->left=tree->left;
                    delete(tree);
                  }
                else
                  {
                    temp->left=NULL;
                    delete(tree);
                    flag=0;
                  }
              }
             else
              {
                 if((tree->right)->right==NULL)
                  {
                    swap(temp,tree->right);
                    if((tree->right)->left!=NULL)
                     {
                       temp=tree->right;
                       tree->right=(tree->right)->left;
                       delete(temp);
                       flag=0;
                     }
                    else
                     {
                       delete(tree->right);
                       tree->right=NULL;
                       flag=0;
                     }
                  }
                 else
                   tree=tree->right;
             }
          }
      
       } 
    }
  }
}

void swap(struct book *t1, struct book *t2)
 {
    char publisher[20],title[20];
    int isbn,year;
    strcpy(publisher,t1->publisher);
    strcpy(title,t1->title);
    isbn=t1->isbn;
    year=t1->year;
    strcpy(t1->publisher,t2->publisher);
    strcpy(t1->title,t2->title);
    t1->isbn=t2->isbn;
    t1->year=t2->year;
    strcpy(t2->publisher,publisher);
    strcpy(t2->title,title);
    t2->isbn=isbn;
    t2->year=year;
 }

int main()
 {
   tree=NULL;
   root=NULL;

   int i;
   cout<<"enter 1 to insert book in the library"<<endl;
   cout<<"enter 2 to search book in the library"<<endl;
   cout<<"enter 3 to delete book from library"<<endl;
   cout<<"enter 0 to exit the program"<<endl;
   cin>>i;
   while(i)
    {
      switch(i)
       {
         case 1: insert();
                 break;
         case 2: cout<<"enter the isbn number of the book"<<endl;
                 cin>>i;
                 tree=search(i);
                 break;
         case 3: cout<<"enter the isbn number of the book"<<endl;
                 cin>>i;
                 delett(i);
                 break;
         default: cout<<"wrong choice encountered"<<endl;
       }
      cout<<"enter 1 to insert book in the library"<<endl;
      cout<<"enter 2 to search book in the library"<<endl;
      cout<<"enter 3 to delete book from the library"<<endl;
      cout<<"enter 0 to exit the program"<<endl;
      cin>>i;
    }
 return 0;
}
