function [f]=FFTR(x)
n=size(x)(2);

if(n==1)
  f=x;
else
  
  f1=FFTR(x(1:2:end));
  f2=FFTR(x(2:2:end));

  for i=1:n
   w(i)=exp(-(j*2*pi*i)/n);
  end

  f1=vertcat(f1,f1);
  f2=vertcat(f2,f2);
  f=complex(f1).+(transpose(w).*complex(f2));
 
endif
endfunction
