#include<iostream>
#include<stdio.h>
using namespace std;


void rejection(float x[],float y[],int n,float mean_x,float mean_y)
 {
   int i,left,right;
   float x1[n],x2[n],y1[n],y2[n];

   left=0;right=0;
   for(i=0;i<n;i++)
    {
      if(x[i] < mean_x)
       {
         x1[left]=x[i];
         y1[left]=y[i];
         left++;
       }
      else
       {
         x2[right]=x[i];
         y2[right]=y[i];
         right++;
       }
    }
   if(left<right)
    {
      n=right;
      left=0;
      right=0;
      for(i=0;i<n;i++)
       {
         if(y2[i] < mean_y)
          {
           x1[left]=x2[i];
           y1[left]=y2[i];
           left++;
          }
         else
          {
           x2[right]=x2[i];
           y2[right]=y2[i];
           right++;
          }
       }
    }

   else
    {
      n=left;
      left=0;
      right=0;
      for(i=0;i<n;i++)
       {
         if(y1[i] < mean_y)
          {
           x1[left]=x1[i];
           y1[left]=y1[i];
           left++;
          }
         else
          {
           x2[right]=x1[i];
           y2[right]=y1[i];
           right++;
          }
       }
     }
   

   if(left<right)
    {
      float x_min,x_max,y_min,y_max;

      if(right>1)
     {
      if(x2[0]<x2[1])
       {x_min=x2[0]; x_max=x2[1];}
      else
       {x_min=x2[1]; x_max=x2[0];}
      

      if(y2[0]<y2[1])
       {y_min=y2[0]; y_max=y2[1];}
      else
       {y_min=y2[1]; y_max=y2[0];}
     }
      else
     { x_min=x2[0]; x_max=x2[0]; 
       y_min=y2[0]; y_max=y2[0];
     }
     

      for(i=2;i<right;i++)
        {
          if(x2[i]> x_max)
           x_max=x2[i];
          else if(x2[i]< x_min)
           x_min=x2[i];
      
          if(y2[i]> y_max)
           y_max=y2[i];
          else if(y2[i]< y_min)
           y_min=y2[i];
        }
       x_min=(x_min + x_max);
       x_min/=2;
       y_min=(y_min + y_max);
       y_min/=2;
       if(right>2)
        rejection(x2,y2,right,x_min,y_min);
       else
        printf("right point is    x=%f    y=%f \n",x_min,y_min);
    }
     

   else
    {
      float x_min,x_max,y_min,y_max;
     if(left>1)
     {
      if(x1[0]<x1[1])
       {x_min=x1[0]; x_max=x1[1];}
      else
       {x_min=x1[1]; x_max=x1[0];}
      

      if(y1[0]<y1[1])
       {y_min=y1[0]; y_max=y1[1];}
      else
       {y_min=y1[1]; y_max=y1[0];}
     }

     else
     { x_min=x1[0]; x_max=x1[0]; 
       y_min=y1[0]; y_max=y1[0];
     }


      for(i=2;i<left;i++)
        {
          if(x1[i]> x_max)
           x_max=x1[i];
          else if(x1[i]< x_min)
           x_min=x1[i];
      
          if(y1[i]> y_max)
           y_max=y1[i];
          else if(y1[i]< y_min)
           y_min=y1[i];
        }
       x_min=(x_min + x_max);
       x_min/=2;
       y_min=(y_min + y_max);
       y_min/=2;

       if(left>2)
        rejection(x1,y1,left,x_min,y_min);
       else
        printf("point is    x=%f    y=%f \n",x_min,y_min);
    }
 }



int main()
 {
   int i,n;
   cout<<"enter the number of coordinates "<<endl;
   cin>>n;
  
   float x[n],y[n],x_min,x_max,y_min,y_max;
   cout<<"enter coordinates"<<endl;
   for(i=0;i<n;i++)
    {
      cin>>x[i]>>y[i];
      cout<<endl;
    }

   if(x[0]<x[1])
       {x_min=x[0]; x_max=x[1];}
      else
       {x_min=x[1]; x_max=x[0];}
      

      if(y[0]<y[1])
       {y_min=y[0]; y_max=y[1];}
      else
       {y_min=y[1]; y_max=y[0];}
      
      for(i=2;i<n;i++)
        {
          if(x[i]> x_max)
           x_max=x[i];
          else if(x[i]< x_min)
           x_min=x[i];
      
          if(y[i]> y_max)
           y_max=y[i];
          else if(y[i]< y_min)
           y_min=y[i];
        }
       x_min=(x_min+x_max)/2;
       y_min=(y_min+y_max)/2;
       /*printf("x=%f    y=%f \n",x_min,y_min);
       cout<<x_min<<"   "<<y_min<<endl;*/
      rejection(x,y,n,x_min,y_min);
 }
     
   













