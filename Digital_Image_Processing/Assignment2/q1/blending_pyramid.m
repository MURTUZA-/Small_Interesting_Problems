function [output]=blending_pyramid(name1,name2,name3,n)
img1=imread(name1);
img2=imread(name2);
mask=imread(name3);
mask./=max(max(mask));
[l_pyramid1,g_pyramid1]=pyramid(img1,n,2,15);
[l_pyramid2,g_pyramid2]=pyramid(img2,n,2,15);
[l_pyramid3,g_pyramid3]=pyramid(mask,n,2,15);

for i=1:n
  output{i}= double((l_pyramid1{i}.*g_pyramid3{i}) .+ (l_pyramid2{i}.*(1.-g_pyramid3{i})));
end

endfunction
