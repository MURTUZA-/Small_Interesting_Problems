function [output]=BCubic_up_sampling(img,sz)
o_sz=size(img);

sx = o_sz(1)/sz(1);
sy = o_sz(2)/sz(2);

  output=zeros(sz(1),sz(2));
  p=ceil(2/sx);
  q=ceil(2/sy);
  for i=p:sz(1)-p
   for j=q:sz(2)-q
     index=[sx*i sy*j];
     x1=floor(index(1))-1;
     x2=floor(index(1));
     x3=ceil(index(1));
     x4=ceil(index(1))+1;
     y1=floor(index(2))-1;
     y2=floor(index(2));
     y3=ceil(index(2));
     y4=ceil(index(2))+1;

     if(x2==x3 || y2==y3)
      if(x2==x3 && y2==y3)
        output(i,j)=img(x2,y2);
      elseif(x2==x3)
        A=[y1^3 y1^2 y1 1;y2^3 y2^2 y2 1;y3^3 y3^2 y3 1;y4^3 y4^2 y4 1];
        Aout=double([img(x2,y1);img(x2,y2);img(x2,y3);img(x2,y4)]);
        wy=inv(A)*Aout;
        A=[index(2)^3 index(2)^2 index(2) 1];     
        output(i,j)=A*wy;
      elseif(y2==y3)
        A=[x1^3 x1^2 x1 1;x2^3 x2^2 x2 1;x3^3 x3^2 x3 1;x4^3 x4^2 x4 1];
        Aout=double([img(x1,y2);img(x2,y2);img(x3,y2);img(x4,y2)]);
        wx=inv(A)*Aout;
        A=[index(1)^3 index(1)^2 index(1) 1];     
        output(i,j)=A*wx;
      endif  
        
     else
     A=[x1^3 x1^2 x1 1;x2^3 x2^2 x2 1;x3^3 x3^2 x3 1;x4^3 x4^2 x4 1];
     invA=inv(A);
     Aout=double([img(x1,y1);img(x2,y1);img(x3,y1);img(x4,y1)]);
     w1=invA * Aout;
     Aout=double([img(x1,y2);img(x2,y2);img(x3,y2);img(x4,y2)]);
     w2=invA*Aout;
     Aout=double([img(x1,y3);img(x2,y3);img(x3,y3);img(x4,y3)]);
     w3=invA*Aout;
     Aout=double([img(x1,y4);img(x2,y4);img(x3,y4);img(x4,y4)]);
     w4=invA*Aout;

     A=[index(1)^3 index(1)^2 index(1) 1];
     w=[w1 w2 w3 w4];
     temp=A*w;

     A=[y1^3 y1^2 y1 1;y2^3 y2^2 y2 1;y3^3 y3^2 y3 1;y4^3 y4^2 y4 1];
     Aout=transpose(temp);
     wy=inv(A)*Aout;
     
     A=[index(2)^3 index(2)^2 index(2) 1];
     
     output(i,j)=A*wy;
     endif
   end
  end
  for i=1:p-1
    output(i,:)=output(p,:);
  end
  for i=1:p
    output(sz(1)-p+i,:)=output(sz(1)-p,:);
  end

  for i=1:q-1
    output(:,i)=output(:,q);
  end
  for i=1:q
    output(:,sz(2)-q+i)=output(:,sz(1)-q);
  end
  
output=uint8(output);
endfunction
