function [output]=High_boost(name,A)

img=imread(name);
lowpass=Gaussian(name,1,3);
highpass=img-lowpass;
output=(A-1)*img + highpass;

endfunction
