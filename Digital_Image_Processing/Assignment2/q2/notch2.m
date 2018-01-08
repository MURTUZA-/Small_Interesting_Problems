function [img,output_fft,H,output]=notch2(name,d)
img=imread(name);
fftimg=fftshift(fft2(img));

sz=size(img);
points=[90,23;53,44;41,108;87,77];

H=ones(sz);
n=size(points)(1);

for k=1:n
  x1=points(k,1)-d;
  x2=points(k,1)+d;

  y1=points(k,2)-d;
  y2=points(k,2)+d;

  if(x1<1) x1=1; endif
  if(x2>sz(1)) x1=sz(1); endif
  if(y1<1) y1=1; endif
  if(y2>sz(2)) y2=sz(2); endif

for i=x1:x2
 for j=y1:y2
  if(((i-points(k,1))^2 + (j-points(k,2))^2)<d)
   H(i,j)=0;
  endif
 end
end
end
output_fft=uint8(abs(fftimg)/sz(1));
output=uint8(abs(ifft2(fftimg.*H)));
endfunction
