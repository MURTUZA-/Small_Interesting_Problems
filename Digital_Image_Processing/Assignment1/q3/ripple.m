function [output]=ripple(name)

img=imread(name);
sz=size(img);
output=zeros(sz(1),sz(2),3);

ax=7;
ay=12;
tx=90;
ty=120;

for k=1:3
for i =1:sz(1)
for j=1:sz(2)

  x= i + ax * sin((2*pi*j)/tx);
  y= j + ax * sin((2*pi*j)/ty);
  
  if(x>=1 && x<=sz(1) && y>=1 && y<=sz(2))
    output(i,j,k)=img(floor(x),floor(y),k);
  endif

end
end
end

output=uint8(output);
imwrite(output,"ripple4.jpg")
endfunction

