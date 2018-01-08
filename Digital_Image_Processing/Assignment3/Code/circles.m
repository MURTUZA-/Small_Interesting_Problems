img=rgb2gray(imread("circle2.jpg"));
sz=size(img);
a=sz(1);
b=sz(2);
r_min=15;
r_max=60;


circular_density=3;
laplacian_threshold=0;


laplacian=edge(img);
Circle=zeros(sz);

parameter_space=zeros(a,b,r_max-r_min+1);

disp("starting parameter");

for p=1:a
for q=1:b
 if(laplacian(p,q)>laplacian_threshold)
  for k=r_min:r_max
   for i=p-k:p+k
     if(i>=1 && i<=a)

       j= round(q + sqrt(k^2 - (i-p)^2));
       if(j<=b) parameter_space(i,j,k-r_min+1)+=1; endif

       j= round(q - sqrt(k^2 - (i-p)^2));
       if(j>=1) parameter_space(i,j,k-r_min+1)+=1; endif

     endif     
    
   end
  end
 endif
end
end

disp("parameter done");
Circle=get_circle(r_min,r_max,parameter_space,circular_density,a,b,sz);
imshow(Circle);
