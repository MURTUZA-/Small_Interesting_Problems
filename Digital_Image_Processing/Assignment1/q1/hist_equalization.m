function [transform]=hist_equalization(x)
Ii=uint8(x);
sz=size(Ii);
N=sz(1)*sz(2);

histogram=imhist(Ii);
prob=cumsum(histogram/N);

transform=uint8(round(prob*255));

endfunction  

