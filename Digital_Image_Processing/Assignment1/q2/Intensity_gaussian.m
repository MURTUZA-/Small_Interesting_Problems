function [I_gaussian]=Intensity_gaussian(intensity,avg_intensity,sigma)
  a = -(((intensity- avg_intensity)^2)/(2*sigma^2));
  I_gaussian=exp(a);
endfunction


