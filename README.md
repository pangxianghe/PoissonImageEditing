Poisson Image Editing
=====
## Seamless Clone
![QQ截图20210626213530](https://user-images.githubusercontent.com/81803879/123514618-76cdce80-d6c6-11eb-8cee-6a47a9fbfd93.png)

Let g be the source image with its gradient vector field v, and S be the target image.

Smooth constraint：
![QQ截图20210626214417](https://user-images.githubusercontent.com/81803879/123514894-b6e18100-d6c7-11eb-92cd-15e083e83dbc.png)


Boundary constraint：
![QQ截图20210626214428](https://user-images.githubusercontent.com/81803879/123514898-bba63500-d6c7-11eb-8d5c-974ef51c30f1.png)

Let : ![QQ截图20210626214627](https://user-images.githubusercontent.com/81803879/123514943-0031d080-d6c8-11eb-8c15-eb6f4f8f5ce5.png)

According to the Euler-Lagrange equation:
![QQ截图20210626214505](https://user-images.githubusercontent.com/81803879/123514907-ca8ce780-d6c7-11eb-9c2a-7afc008b3711.png)

refer to：
https://zhuanlan.zhihu.com/p/20718489

Substitute into the equation:
![QQ截图20210626214554](https://user-images.githubusercontent.com/81803879/123514929-e85a4c80-d6c7-11eb-92c8-21fde07f939e.png)

F is the function of ▽ F，rather than f：

![QQ截图20210626214258](https://user-images.githubusercontent.com/81803879/123514855-80a40180-d6c7-11eb-9bc0-1b87843fe5b9.png)

![QQ截图20210626214335](https://user-images.githubusercontent.com/81803879/123514871-944f6800-d6c7-11eb-9e6d-45cf05701c09.png)




## Discrete_Poisson_equation：
Refer to：https://en.wikipedia.org/wiki/Discrete_Poisson_equation

![QQ截图20210626222914](https://user-images.githubusercontent.com/81803879/123516311-075bdd00-d6ce-11eb-9a1b-fc2fc738fec6.png)
![QQ截图20210626222925](https://user-images.githubusercontent.com/81803879/123516313-0925a080-d6ce-11eb-924f-6dbfa93b849a.png)

## Results：

### source   &   mask   &   target：：

![leber-source](https://user-images.githubusercontent.com/81803879/123516484-d16b2880-d6ce-11eb-8a7f-523e03d6304e.jpg)
![mona-mask](https://user-images.githubusercontent.com/81803879/123516486-d4feaf80-d6ce-11eb-8c2a-ce65f436a251.jpg)
![mona-target](https://user-images.githubusercontent.com/81803879/123516490-dd56ea80-d6ce-11eb-8caf-9bf61de32264.jpg)

### SeamlessClone   &   NaiveClone：

![result](https://user-images.githubusercontent.com/81803879/123516406-82bd8e80-d6ce-11eb-9b85-970b5cbf8851.png)
![result_naive](https://user-images.githubusercontent.com/81803879/123516439-a7b20180-d6ce-11eb-93af-743a55d5c9b3.png)


### source   &   mask：

![bear](https://user-images.githubusercontent.com/81803879/123515127-d75e0b00-d6c8-11eb-8ec7-6749e2010e66.jpg)
![bear-mask](https://user-images.githubusercontent.com/81803879/123515132-d9c06500-d6c8-11eb-87a0-1ff33b926ac3.jpg)

### target   &   SeamlessClone   &   NaiveClone：：

![pool-target](https://user-images.githubusercontent.com/81803879/123516537-2f980b80-d6cf-11eb-86ba-230ddff16d40.jpg)
![result](https://user-images.githubusercontent.com/81803879/123516526-13946a00-d6cf-11eb-9884-5624824c9046.png)
![result_naive](https://user-images.githubusercontent.com/81803879/123516529-1727f100-d6cf-11eb-9cfd-c1825847a62a.png)


