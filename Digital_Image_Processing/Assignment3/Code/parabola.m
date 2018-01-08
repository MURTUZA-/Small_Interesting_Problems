img=rgb2gray(imread("circle2.jpg"));
sz=size(img);
a=sz(1);
b=sz(2);
m_min=-20;
m_max=20;
c_min=-20;
c_max=20;


circular_density=10;
laplacian_threshold=0;


laplacian=edge(img);
parabola=zeros(sz);

parameter_space=zeros(a,b,m_max-m_min+1,c_max-c_min+1);

disp("starting parameter");

for p=1:sz(1)
for q=1:sz(2)
 if(laplacian(p,q)>laplacian_threshold)
  for k=1:a
   for i=1:b
    for j=m_min:m_max
     l= sqrt(((p-k)^2+(q-i)^2)*(1+j^2))-q+j*p;
     if(l>=c_min && l<=c_max)
       parameter_space(k,i,j-m_min+1,l-c_min+1)+=1;
     endif
     l=-l;
     if(l>=c_min && l<=c_max)
       parameter_space(k,i,j-m_min+1,l-c_min+1)+=1;
     endif
    
   end
  end
 end
 endif
end
end

disp("parameter done");
parabola=get_parabola(r_min,r_max,parameter_space,circular_density,a,b,sz);
imshow(Circle);
