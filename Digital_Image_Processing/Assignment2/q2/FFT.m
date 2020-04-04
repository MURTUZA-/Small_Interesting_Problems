function [f]=FFT(x)
  n=size(x)(2);
  k=ceil(log2(n));
  n1= 2^k;
  y=zeros(1,n1-n);
  x=horzcat(y,x);
  f=FFTR(x);
  f=f(1:n);
endfunction

