function [output]=laplacian(ft)
[row,col]=size(ft);
output=zeros(row,col);
for i=1:row
  for j=1:col
    output(i,j)=-((i^2+j^2)*ft(i,j))/((row)*(col));
  end
end
output=fftshift(output);
output=uint8(abs(ifft2(output)));
endfunction
