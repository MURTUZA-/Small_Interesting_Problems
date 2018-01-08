function [img,output_fft,H,output]=notch1(name)
img=imread(name);
fftimg=fftshift(fft2(img));

sz=size(img);
H=ones(sz(1),sz(2));
x=zeros(1,sz(2));

for i=74:85
 H(i,:)=x;
end
 
for i=174:185
 H(i,:)=x;
end
for i=130:142
  H(1:87,i)=0;
end

for i=158:162
  H(1:87,i)=0;
  H(166:end,i)=0;
end

for i=166:174
  H(1:87,i)=0;
end

for i=144:153
  H(166:end,i)=0;
end

for i=180:190
  H(166:end,i)=0;
end
output_fft=uint8(abs(fftimg)/sz(1));
output=uint8(abs(ifft2(fftimg.*H)));
endfunction
