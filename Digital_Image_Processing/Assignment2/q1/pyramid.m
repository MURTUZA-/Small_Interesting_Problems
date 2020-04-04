function [L_pyramid,G_pyramid]=pyramid(Img,n,sigma, window)

for i=1:n-1
 img=Gaussian(Img,sigma,window);
 L_pyramid{i}=(Img.-img);
 G_pyramid{i}=(Img);
 if(size(size(Img))(2)==3)
  Img=img(1:2:end,1:2:end,:);
 else
  Img=img(1:2:end,1:2:end);
 endif

end
L_pyramid{n}=(Img);
G_pyramid{n}=(Img);
endfunction
