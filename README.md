Poisson Image Editing
=====
## 泊松图像编辑
![QQ截图20210626213530](https://user-images.githubusercontent.com/81803879/123514618-76cdce80-d6c6-11eb-8cee-6a47a9fbfd93.png)

其中g是前景图片，v是其梯度场，S是目标背景图片

满足前景尽量平滑，有：
![QQ截图20210626214417](https://user-images.githubusercontent.com/81803879/123514894-b6e18100-d6c7-11eb-92cd-15e083e83dbc.png)


满足边界一致，有：
![QQ截图20210626214428](https://user-images.githubusercontent.com/81803879/123514898-bba63500-d6c7-11eb-8d5c-974ef51c30f1.png)

令      
![QQ截图20210626214627](https://user-images.githubusercontent.com/81803879/123514943-0031d080-d6c8-11eb-8c15-eb6f4f8f5ce5.png)

由欧拉-拉格朗日方程：
![QQ截图20210626214505](https://user-images.githubusercontent.com/81803879/123514907-ca8ce780-d6c7-11eb-9c2a-7afc008b3711.png)

方程证明见：
https://zhuanlan.zhihu.com/p/20718489

代入方程：
![QQ截图20210626214554](https://user-images.githubusercontent.com/81803879/123514929-e85a4c80-d6c7-11eb-92c8-21fde07f939e.png)

注意到F是关于▲f的函数，而不是f：

![QQ截图20210626214258](https://user-images.githubusercontent.com/81803879/123514855-80a40180-d6c7-11eb-9bc0-1b87843fe5b9.png)

![QQ截图20210626214335](https://user-images.githubusercontent.com/81803879/123514871-944f6800-d6c7-11eb-9e6d-45cf05701c09.png)




## 离散泊松方程解法：
### 参考：https://en.wikipedia.org/wiki/Discrete_Poisson_equation
![QQ截图20210626213325](https://user-images.githubusercontent.com/81803879/123514553-2c4c5200-d6c6-11eb-81f4-158d4328c565.png)
![QQ截图20210626213331](https://user-images.githubusercontent.com/81803879/123514558-2f474280-d6c6-11eb-86e6-2fb4e8e1df4e.png)

## Results：

### source   &   mask   &   target：：

![QQ截图20210626220337](https://user-images.githubusercontent.com/81803879/123515534-63bcfd80-d6ca-11eb-9c00-538960446905.png)
![QQ截图20210626220435](https://user-images.githubusercontent.com/81803879/123515570-851de980-d6ca-11eb-9a68-b30bd8d66ff9.png)
![QQ截图20210626220246](https://user-images.githubusercontent.com/81803879/123515505-41c37b00-d6ca-11eb-99df-d93e56dd09ab.png)

### SeamlessClone   &   NaiveClone：

![QQ截图20210626220513](https://user-images.githubusercontent.com/81803879/123515607-a4b51200-d6ca-11eb-965a-b443a0d95433.png)
![QQ截图20210626220526](https://user-images.githubusercontent.com/81803879/123515612-a7b00280-d6ca-11eb-902c-39464b19cca0.png)



### source   &   mask：

![bear](https://user-images.githubusercontent.com/81803879/123515127-d75e0b00-d6c8-11eb-8ec7-6749e2010e66.jpg)
![bear-mask](https://user-images.githubusercontent.com/81803879/123515132-d9c06500-d6c8-11eb-87a0-1ff33b926ac3.jpg)

### target   &   SeamlessClone   &   NaiveClone：：

![pool-target](https://user-images.githubusercontent.com/81803879/123515141-dc22bf00-d6c8-11eb-9053-465624aa77d1.jpg)
![result](https://user-images.githubusercontent.com/81803879/123515160-e1800980-d6c8-11eb-8019-608fdc0b0eac.png)
![result_naive](https://user-images.githubusercontent.com/81803879/123515168-e47afa00-d6c8-11eb-9e32-e5303ae7eb46.png)


