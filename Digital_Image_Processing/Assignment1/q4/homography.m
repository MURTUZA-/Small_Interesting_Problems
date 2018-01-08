I=imread("stereo_pair.jpg");
for i=1:3
I1(:,:,i)=I(:,1:floor(size(I)(2)/2),i);
I2(:,:,i)=I(:,floor(size(I)(2)/2)+1:size(I)(2),i);
end
output=zeros(size(I1)(1),size(I1)(2),3);

#A is projective transformation matrix
A=zeros(3);

#Manually obeserved correspoinding points in left and right image
points1=[1193,485,1;423,84,1;60,1283,1];
points2=[1263,487,1;495,89,1;116,1285,1];

A(1,:)=transpose( inv(points1) * points2(:,1) );
A(2,:)=transpose( inv(points1) * points2(:,2) );
A(3,:)=transpose( inv(points1) * points2(:,3) );

invA=inv(A);

for y=1:size(I1)(1)
for x=1:size(I1)(2)
   v=[x;y;1];
   v=invA*v;
   j=floor(v(1));
   i=floor(v(2));
   if(i>=1 && i<=size(I1)(1) && j>=1 && j<=size(I1)(2))
    for p=1:3
     output(y,x,p)=I1(i,j,p);
    end
   endif
end
end


output=uint8(output);
