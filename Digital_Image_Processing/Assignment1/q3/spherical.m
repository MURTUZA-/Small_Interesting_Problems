function [output]=spherical(name)

img=imread(name);
sz=size(img);
output=zeros(sz(1),sz(2),3);

xc=sz(1)/2;
yc=sz(2)/2;
rmax=160;
p=2;


for k=1:3
for i =1:sz(1)
for j=1:sz(2)

dx=i-xc;
dy=j-yc;
r=sqrt(dx^2 + dy^2);
z=sqrt(rmax^2 - r^2);

betax=(1-1/p)* asin(dx/sqrt((dx^2)+(z^2)));
betay=(1-1/p)* asin(dy/sqrt((dy^2)+(z^2)));

if(r<rmax)
 x=i-(z*tan(betax));
 y=j-(z*tan(betay));
else
 x=i;
 y=j;
endif

  if(x>=1 && x<=sz(1) && y>=1 && y<=sz(2))
    output(i,j,k)=img(floor(x),floor(y),k);
  endif

end
end
end

output=uint8(output);
imwrite(output,"spherical4.jpg");
endfunction

