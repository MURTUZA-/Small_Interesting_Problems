function [img,output_fft,H,output]=notch3(name)
img=imread(name);
fftimg=fftshift(fft2(img));

sz=size(img);

H=ones(sz(1),sz(2));

for i=126:133
 H(1:90,i)=0;
 H(176:256,i)=0;
end

for i=126:133
 H(i,1:90)=0;
 H(i,176:256)=0;
end

output_fft=uint8(abs(fftimg)/sz(1));
output=uint8(abs(ifft2(fftimg.*H)));
endfunction
