function [output]=NN_up_sampling(Img,sz)
o_sz=size(Img);

sx = o_sz(1)/sz(1);
sy = o_sz(2)/sz(2);

if(size(o_sz)(2)!=3)
  output=zeros(sz(1),sz(2));
  p=ceil(.5/sx);
  q=ceil(.5/sy);
  output(1:p-1,1:q-1)=Img(1,1);
  for i=p:sz(1)
   for j=q:sz(2)
     index=[round(sx*i) round(sy*j)];
     output(i,j)=Img(index(1),index(2));
   end
  end
else
  output=zeros(sz(1),sz(2),3);
  p=ceil(.5/sx);
  q=ceil(.5/sy);
  output(1:p-1,1:q-1,1)=Img(1,1,1);
  output(1:p-1,1:q-1,2)=Img(1,1,2);
  output(1:p-1,1:q-1,3)=Img(1,1,3);
  for i=p:sz(1)
   for j=q:sz(2)
     index=[round(sx*i) round(sy*j)];
     output(i,j,:)=Img(index(1),index(2),:);
   end
  end
endif
output=uint8(output);
endfunction
