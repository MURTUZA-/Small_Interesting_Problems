img=imread("image1.jpg");
sz=size(img);
patch_size=15;
half=floor(patch_size/2);
output=0;


for i=half:sz(1)-half-1
  for j=half:sz(2)-half-1
   
    mat=0;
    for l=1:patch_size
      for k=1:patch_size
          mat(l,k)=img(i-half+l,j-half+k);
      end
     end

     transform=hist_equalization(mat);
     output(i,j) = transform(img(i,j)+1);

  end
end

output=uint8(output);
imshow(output);
imwrite(output,"result_image1.jpg");
