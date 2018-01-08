function [x_matched_to_y,histogram]=hist_matching(name1,name2)

x=imread(name1);
y=imread(name2);
transform1=hist_equalization(x);
transform2=hist_equalization(y);

matching_transform=zeros(size(transform1)(1),1);

for i=1:size(transform1)(1)
  for j=1:size(transform2)(1)
    if (transform1(i)<=transform2(j))
      matching_transform(i)=j;
      break;
    endif
  end
end

for i=1:size(x)(1)
  for j=1:size(x)(2)
   x_matched_to_y(i,j)=matching_transform(x(i,j)+1);
  end
end

x_matched_to_y = uint8(x_matched_to_y);
histogram=imhist(x_matched_to_y);
imwrite(x_matched_to_y,"output.jpg");

endfunction
