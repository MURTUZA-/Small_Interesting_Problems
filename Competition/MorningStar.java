/*

Morningstar Logo
Annual Party!

Morningstar India holds an annual party at the end of every year in December. Most of the attendees are Morningstar employees. In preparation, the fun idea team, who help as organizers, have to make a drink that most of the attendees may like. They propose to make a drink by mixing together three different types of fruit juice: Apple, Banana and Carrot. Let's name the juices A, B and C.
The fun idea team wants to decide what fraction of the drink should be made from each type of juice, in such a way that the maximum possible number of people attending the party like it.
Not being able to arrive at a common decision, they launch a survey to hear what employees would like. As a survey feedback they expect each attendee to respond and mention a minimum fraction of each of the 3 juices they would like to have in the drink. Fun Idea team knows that they will only like the drink if the fraction of each of the 3 juices in the drink is greater or equal to their minimum fraction for that juice.
Can you help our fun idea team determine the maximum number of people that they can satisfy?
Input file sample

	3
	3
	10000 0 0
	0 10000 0
	0 0 10000
	3
	5000 0 0
	0 2000 0
	0 0 4000
	5
	0 1250 0
	3000 0 3000
	1000 1000 1000
	2000 1000 2000
	1000 3000 2000
Input

One line containing an integer T, the number of test cases in the input file.
For each test case, there will be:
One line containing the integer N, the number of people going to the party. N lines, one for each person, each containing three space-separated numbers "A B C", indicating the minimum fraction of each juice that one would like in the drink. A, B and C are integers between 0 and 10000 inclusive, indicating the fraction in parts-per-ten-thousand. A + B + C ≤ 10000.
Output sample

	Case #1: 1
	Case #2: 2
	Case #3: 5
T lines, one for each test case in the order they occur in the input file, each containing the string "Case #X: Y" where X is the number of the test case, starting from 1, and Y is the maximum number of people who will like your drink.



*/

import java.util.Scanner;

class MorningStar{
public static void main(String args[]){


   int n,i,k,j,T;
   Scanner in=new Scanner (System.in);
   T=in.nextInt();
   int max[]=new int[T];
   
   for(j=0;j<T;j++){

	   n=in.nextInt();
	   
	   int count[]=new int[n*n*n];


	   int a1[]=new int[n];
	   int a2[]=new int[n];
	   int a3[]=new int[n];

	   
	   for(i=0;i<n*n*n;i++){
	   count[i]=0;
   }
   
   int arr[][]=new int[n][3];
   String S[]=new String[3];
   String s;
   s=in.nextLine();
   
   for(i=0;i<n;i++){
   s=in.nextLine();
   S=s.split("\\s+");
	arr[i][0]=Integer.parseInt(S[0]);
	arr[i][1]=Integer.parseInt(S[1]);
	arr[i][2]=Integer.parseInt(S[2]);
   }
  
   int A1,A2,A3=0;
   A1=0;
   A2=0;
   for(i=0;i<n;i++){
   a1[i]=arr[i][0];
   a2[i]=arr[i][1];
   a3[i]=arr[i][2];
   }
	   for(k=0;k<n;k++)
	   for(i=0;i<n-1;i++){
		   if(a1[i]< a1[i+1]){
			   int h=a1[i];
			   a1[i]=a1[i+1];
			   a1[i+1]=h;
		   }
		   if(a2[i]< a2[i+1]){
			   int h=a2[i];
			   a2[i]=a2[i+1];
			   a2[i+1]=h;
		   }
		   if(a3[i]< a3[i+1]){
			   int h=a3[i];
			   a3[i]=a3[i+1];
			   a3[i+1]=h;
		   }
	   }
	   k=n;int h;
	   for(i=0;i<k-1;i++){
		   if(a1[i]==a1[i+1]){for(h=i;h<k-1;h++) a1[h]=a1[h+1]; k--;i--;}
	   }
	   A1=k-1;
	   
	   k=n;
	   for(i=0;i<k-1;i++){
		   if(a2[i]==a2[i+1]){for(h=i;h<k-1;h++) a2[h]=a2[h+1]; k--;i--;}
	   }
	   A2=k-1;

	   k=n;
	   for(i=0;i<k-1;i++){
		   if(a3[i]==a3[i+1]){for(h=i;h<k-1;h++) a3[h]=a3[h+1]; k--;i--;}
	   }
	   A3=k-1;
	   
	   



i=0;
   k=0;
   int l=0;
   int c=0;
   while(l<=A3){
	   while(k<=A2){ i=0;
		   while(i<=A1){
			   if(a1[i]+a2[k]+a3[l]<=10000){
				   
				   for(int f=0;f<n;f++){
				       if(arr[f][0]<=a1[i] && arr[f][1]<=a2[k] && arr[f][2]<=a3[l])
					    count[c]=count[c]+1;
				       
				   }
				   c++;
				   if(i==0){if(k==0 && l==0){i=A1+1;k=A2+1;l=A3+1;} else {if(l<A3){l++;k=0;} else{i=A1+1;k=A2+1;l=A3+1;}} }
				   else {if(k<A2){k++;i=0;} else {if(l<A3){l++;k=0;i=0;} else{l=A3+1;k=A2+1;i=A1+1;} }}
				   
			   }
			   else{i++;}
			   			   			   
		   } k++;
	   } l++;
   }
  
   
	   max[j]=0;
   for(i=0;i<c;i++){
      if(count[i]>max[j])
    	  max[j]=count[i];
   }
   
  }   
for(j=1;j<=T;j++){
   System.out.println("Case #" + j + ": " + max[j-1]);
}
   in.close();
}

}
