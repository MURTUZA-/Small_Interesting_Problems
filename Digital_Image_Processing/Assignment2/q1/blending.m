function [pyramid]=blending(name1,name2,name3,n)

pyramid=blending_pyramid(name1,name2,name3,n);

for i=1:n-1
  x=imresize(uint8(pyramid{n-i+1}),[size(pyramid{n-i})(1),size(pyramid{n-i})(2)]); 
#  x=BL_up_sampling(uint8(pyramid{n-i+1}),[size(pyramid{n-i})(1),size(pyramid{n-i})(2)]);
  pyramid{n-i}= x .+ pyramid{n-i};
end
endfunction
