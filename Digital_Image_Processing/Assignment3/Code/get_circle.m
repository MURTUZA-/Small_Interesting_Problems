function Circle=get_circle(r_min,r_max,parameter_space,circular_density,a,b,sz)
Circle=zeros(sz);
k=r_min;
while(k<=r_max)
   
   [max_val,ind]=max(parameter_space(:,:,k-r_min+1)(:));
   [i,j]=ind2sub(size(parameter_space(:,:,k-r_min+1)),ind);
   if(max_val>(circular_density*k))
     k
     for p=i-k:i+k
       q= round(j + sqrt(k^2 - (p-i)^2));
       if(q<=b && p>=1 && p<=a) Circle(p,q)=1; endif

       q= round(j - sqrt(k^2 - (p-i)^2));
       if(q>=1 && p>=1 && p<=a) Circle(p,q)=1; endif

     end
     parameter_space(i,j,k-r_min+1)=-1;
     k=k-1;

    endif
k+=1;
end
endfunction
