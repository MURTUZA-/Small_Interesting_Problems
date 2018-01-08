function [f]=FFT2(img,n1,n2)
k1=ceil(log2(n1));
k2=ceil(log2(n2));
n11=2^k1;
n22=2^k2;
f=FFT2R(img,n11,n22);
f=f(1:n1,1:n2);
f=fftshift(f);
endfunction
