img=imread("bilateral.jpg");
img=img(:,:,1);
I_sigma=10;
S_sigma=1;
filter_size=3;
half=floor(filter_size/2)+1;

sz=size(img);
avg_intensity=sum(sum(img))/(sz(1)*sz(2));

img1=Gaussian("bilateral.jpg",S_sigma,filter_size);

img2=0;

for i=1:sz(1)
for j=1:sz(2)

  I_filter=0;
  t=0;
  for l=1:filter_size
  for k=1:filter_size
    if ((!( (i-half+l)<1 || (i-half+l)>sz(1) )) && (!( (j-half+k)<1 || (j-half+k)>sz(2) )))
      I_filter(t+1)=Intensity_gaussian(img(i-half+l,j-half+k),avg_intensity,I_sigma) * img(i-half+l,j-half+k);
      t++;
    endif
  end
  end

  img2(i,j)=sum(I_filter);

end
end

output=0.65*img1+.35*img2;

