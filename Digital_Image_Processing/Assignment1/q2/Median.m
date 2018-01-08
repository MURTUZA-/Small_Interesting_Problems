function [output]=Median(name,filter_size)
img=imread(name);
sz=size(img);

output=0;
for i=1:sz(1)
for j=1:sz(2)
t=0;
mdn=0;
  for l=1:filter_size
    for k=1:filter_size
       a=i - (floor(filter_size/2) + 1) + l;
       b=j - (floor(filter_size/2) + 1) + k;
       if(!(a<1 || a>sz(1)))
         if(!(b<1 || b>sz(2)))
           mdn(t+1)=img(a,b);
           t++;
         endif
       endif

    end
  end
  mdn=sort(mdn);
  output(i,j)=mdn(floor(t/2)+1);
end
end
output=uint8(output);
endfunction
