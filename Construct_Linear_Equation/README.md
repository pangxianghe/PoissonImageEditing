Poisson Image Editing
=====
## Seamless Clone:
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

## Mixing Gradient Clone:

![QQ截图20210629202914](https://user-images.githubusercontent.com/81803879/123797376-b12eaa00-d918-11eb-8fda-fbb624627344.png)

## Texture Flattening:

![20210629202631](https://user-images.githubusercontent.com/81803879/123797019-585f1180-d918-11eb-92a2-4bf8488842cf.png)

## Local Illumination Change:

![QQ截图20210629202749](https://user-images.githubusercontent.com/81803879/123797157-7b89c100-d918-11eb-9112-b7458f6c784b.png)

## Local Color Change:

Change the gradient of the source or target image.



## Discrete_Poisson_equation：

### The equation can be solved in two ways: 
#### By forming the Ax = b linear equation:

Dirichlet Boundary

Refer to：https://en.wikipedia.org/wiki/Discrete_Poisson_equation

![QQ截图20210626222914](https://user-images.githubusercontent.com/81803879/123516311-075bdd00-d6ce-11eb-9a1b-fc2fc738fec6.png)
![QQ截图20210626222925](https://user-images.githubusercontent.com/81803879/123516313-0925a080-d6ce-11eb-924f-6dbfa93b849a.png)

#### By DST:
This way is faster and adopted by OpenCV

Neumann Boundary

Refer to https://elonen.iki.fi/code/misc-notes/neumann-cosine/

![20210524105219686 (1](https://user-images.githubusercontent.com/81803879/123796723-fef6e280-d917-11eb-9af5-f113c762051f.png)


![QQ截图20210629202149](https://user-images.githubusercontent.com/81803879/123796370-a6bfe080-d917-11eb-81aa-70fbbaa60f0a.png)

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

### Seamless Clone   &   Mixing Gradients Clone   :

![test3_src](https://user-images.githubusercontent.com/81803879/123795430-99562680-d916-11eb-87bf-8befbb705061.jpg)
![test3_target](https://user-images.githubusercontent.com/81803879/123795591-bf7bc680-d916-11eb-95a5-71b688361c99.jpg)
![test3_mix_result](https://user-images.githubusercontent.com/81803879/123795600-c1de2080-d916-11eb-9663-5af873535fa6.jpg)
![test3_result](https://user-images.githubusercontent.com/81803879/123795605-c3a7e400-d916-11eb-9d94-1444f1c0718d.jpg)

### Texture Flattening   ：

![test4_src](https://user-images.githubusercontent.com/81803879/123795840-049ff880-d917-11eb-96ab-301d7e24a459.jpg)
![test4_flatten_result](https://user-images.githubusercontent.com/81803879/123795795-f8b43680-d916-11eb-8e0f-57f2ea8d3e18.jpg)

### Local Illumination Change   ：

![test5_src](https://user-images.githubusercontent.com/81803879/123795938-24372100-d917-11eb-9724-f68e50254deb.jpg)
![test5_illu_result](https://user-images.githubusercontent.com/81803879/123795946-2600e480-d917-11eb-8428-4fa04f75d5c1.jpg)

## Local Color Change   :

![test6_src](https://user-images.githubusercontent.com/81803879/123795279-70359600-d916-11eb-916d-e48baf1608de.png)
![test6](https://user-images.githubusercontent.com/81803879/123795284-7166c300-d916-11eb-90b9-2e4383eabdf2.png)






