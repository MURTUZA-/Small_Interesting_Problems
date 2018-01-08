function [output]=ideal_lp(sz,d)
output=zeros(sz);
row=sz(1);
col=sz(2);
cx=floor(col/2);
cy=floor(row/2);
for i=1:row
  for j=1:col
    if (d< sqrt((i-cy)^2 + (j-cx)^2))
      output(i,j)=0;
    else
      output(i,j)=1;
    endif
  end
end
endfunction
