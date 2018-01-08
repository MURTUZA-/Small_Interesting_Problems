function [output]=linear(Img)
o_sz=size(Img);

sx = .5;
sy = .5;
n1=o_sz(1)*2;
n2=o_sz(2)*2;

if(size(o_sz)(2)!=3)
  output=zeros(n1,n2);
  output(1:2:n1,1:2:n2)=Img(:,:);
  for i=1:2:n1
  for j=2:2:n2
    if(j==n2)
      output(i,j)=output(i,j-1);
    else
      output(i,j)=(output(i,j+1)+output(i,j-1))/2;
    endif
  end
  end

  for i=2:2:n1
  for j=1:2:n2
    if(i==n1)
      output(i,j)=output(i-1,j);
    else
      output(i,j)=(output(i+1,j)+output(i-1,j))/2;
    endif
  end
  end

  for i=2:2:n1
  for j=2:2:n2
    if(i==n1 || j==n2)
      if(i==n1 && j==n2)
        output(i,j)=(output(i-1,j)+output(i,j-1))/2;
      elseif(i==n1)
        output(i,j)=(output(i-1,j)+output(i,j+1)+output(i,j-1))/3;
      else
        output(i,j)=(output(i-1,j)+output(i+1,j)+output(i,j-1))/3;
      endif
    else
      output(i,j)=(output(i-1,j)+output(i+1,j)+output(i,j-1)+output(i,j+1))/4;
    endif
  end
  end


else
  output=zeros(n1,n2,3);
  output(1:2:n1,1:2:n2,:)=Img(:,:,:);
  for i=1:2:n1
  for j=2:2:n2
    if(j==n2)
      output(i,j,:)=output(i,j-1,:);
    else
      output(i,j,:)=(output(i,j+1,:).+output(i,j-1,:))/2;
    endif
  end
  end

  for i=2:2:n1
  for j=1:2:n2
    if(i==n1)
      output(i,j,:)=output(i-1,j,:);
    else
      output(i,j,:)=(output(i+1,j,:).+output(i-1,j,:))/2;
    endif
  end
  end

  for i=2:2:n1
  for j=2:2:n2
    if(i==n1 || j==n2)
      if(i==n1 && j==n2)
        output(i,j,:)=(output(i-1,j,:).+output(i,j-1,:))/2;
      elseif(i==n1)
        output(i,j,:)=(output(i-1,j,:).+output(i,j+1,:)+output(i,j-1,:))/3;
      else
        output(i,j,:)=(output(i-1,j,:).+output(i+1,j,:).+output(i,j-1,:))/3;
      endif
    else
      output(i,j,:)=(output(i-1,j,:).+output(i+1,j,:).+output(i,j-1,:).+output(i,j+1,:))/4;
    endif
  end
  end

endif
output=uint8(output);
endfunction
