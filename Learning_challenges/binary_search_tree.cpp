#include<iostream>
using namespace std;
struct node
{
	int data;
	node *left;
	node *right;
};
node *tree=NULL;
int count=0;

void insert(int x)
 {
	 node *t;
	 if(tree==NULL)
	  {
		  t=new node;
		  t->data=x;
		  t->left=NULL;
		  t->right=NULL;
		  tree=t;
		  count++;
	  }
	 else
	  {
		  int i,q=1;
		  t=tree;
		  node *t1;
		  for(i=0;i<count && q!=0;i++)
		    {
				if(t->data>x)
				 {
				    if(t->left!=NULL)
				      t=t->left;
				    else
				     {
					   t1= new node;
					   t1->data=x;
					   t1->left=NULL;
					   t1->right=NULL;
					   t->left=t1;
					   count++;
					   q=0;
				     }
				 }
				else
				 {
					 if(t->right!=NULL)
					   t=t->right;
					 else
					  {
						 t1=new node;
						 t1->data=x;
						 t1->left=NULL;
						 t1->right=NULL;
						 t->right=t1;
						 count++;
						 q=0;
					   }
				  }
			  }
		 }
  }
  
 void search(int x)
  {
	  if(tree==NULL)
	    cout<<"tree is empty"<<endl;
	  else
	    {
		   int i=0;int q=1;
		   node *t=tree;
		   while(i<count && q!=0)
		    {
				if(t->data==x)
				{
					cout<<"element is found at height = "<<i<<endl;
					q=0;
				}
				else
				 {
					if(t->data>x)
					 {
						if(t->left!=NULL)
						  t=t->left;
						else
						  {
							 cout<<"element is not found"<<endl;
							 q=0;
						  }
					 }
					else
					 {
						if(t->right!=NULL)
						  t=t->right;
						else
						  {
							 cout<<"element is not found"<<endl;
							 q=0;
						  }
					 }
				  }
				i++;
			}
		 }
   }


 int height(node *p)
  {
    if(p->left==NULL && p->right==NULL)
     return 1;
    else
     {

       int countl,countr=0;
       countl=0;

       if(p->left != NULL)
        countl = 1+ height(p->left);
   
       if(p->right != NULL)
        countr=1+height(p->right);
  

       if(countr<countl)
         return (countl);
       else
         return(countr);
     }
  }




				 
main()
{
	int n;
	cout<<"enter the no. of elements"<<endl;
	cin>>n;
	int a[n],i;
	cout<<"enter the "<<n<<" integer values"<<endl;
	for(i=0;i<n;i++)
	 {
		 cin>>a[i];
	     insert(a[i]);
	 }
	cout<<"tree is created"<<endl;
	cout<<"------*****------"<<endl;
	cout<<"enter 1 to search an element in the tree"<<endl;
        cout<<"enter 2 to calculate the height of tree"<<endl;
	cin>>i;
	if(i==1)
	 {
		cout<<"enter integer value to be searched in the tree"<<endl;
		cin>>i;
		search(i);
	 }
        else
         {
           i=height(tree)-1;
           cout<<"height of the tree is----  "<<i<<endl;
         }
}
	
