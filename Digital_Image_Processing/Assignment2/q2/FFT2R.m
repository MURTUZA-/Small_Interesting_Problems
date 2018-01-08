function [f]=FFT2R(img,n1,n2)
s=[n1 n2];
img=imresize(img,s);
temp=FFT(img(1,:));
for i=2:n1
 temp=horzcat(temp,FFT(img(i,:)));
end
temp=transpose(temp);

for i=1:n2
 temp(:,i)=FFT(transpose(temp(:,i)));
end

f=temp;
endfunction
