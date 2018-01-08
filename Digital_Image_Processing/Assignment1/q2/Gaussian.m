function [img]=Gaussian(name,sigma,filter_size)
img=imread(name);

for i=1:filter_size
  for j=1:filter_size
    a=-(((i - (floor(filter_size/2) + 1))^2) + ((j - (floor(filter_size/2) + 1))^2)) / (2 * sigma^2);
    fltr(i,j)=exp(a);
  end
end

fltr=(1/sum(sum(fltr)))*fltr;
img=convn(img,fltr,'same');
img=uint8(img);
endfunction
