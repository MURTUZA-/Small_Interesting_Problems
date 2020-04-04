function [output]=BL_up_sampling(img,sz)
o_sz=size(img);

sx = o_sz(1)/sz(1);
sy = o_sz(2)/sz(2);

if(size(o_sz)(2)!=3)
  output=zeros(sz(1),sz(2));
  p=ceil(1/sx);
  q=ceil(1/sy);
  output(1:p-1,1:q-1)=img(1,1);
  for i=p:sz(1)
   for j=q:sz(2)
     index=[sx*i sy*j];
     x1=floor(index(1));
     x2=ceil(index(1));
     y1=floor(index(2));
     y2=ceil(index(2));
     intensity1= img(x1,y1) + (img(x2,y1)-img(x1,y1))*(index(1)-x1);
     intensity2= img(x1,y2) + (img(x2,y2)-img(x1,y2))*(index(1)-x1);
     intensity3= intensity1 + (intensity2-intensity1)*(index(2)-y1);
     output(i,j)=intensity3;
   end
  end
else
  output=zeros(sz(1),sz(2),3);
  p=ceil(1/sx);
  q=ceil(1/sy);
  output(1:p-1,1:q-1,1)=img(1,1,1);
  output(1:p-1,1:q-1,2)=img(1,1,2);
  output(1:p-1,1:q-1,3)=img(1,1,3);
  for i=p:sz(1)
   for j=q:sz(2)
     index=[sx*i sy*j];
     x1=floor(index(1));
     x2=ceil(index(1));
     y1=floor(index(2));
     y2=ceil(index(2));
     intensity1= img(x1,y1,:) .+ ((img(x2,y1,:).-img(x1,y1,:)).*(index(1)-x1));
     intensity2= img(x1,y2,:) .+ ((img(x2,y2,:).-img(x1,y2,:)).*(index(1)-x1));
     intensity3= intensity1 .+ ((intensity2.-intensity1).*(index(2)-y1));
     output(i,j,:)=intensity3;
   end
  end
endif
output=uint8(output);
endfunction
