## 电影推荐系统

一个简易的电影推荐系统，包括用户注册登陆，展示电影信息，为我推荐电影，我的观影记录四个模块。

### 参考内容

* [https://github.com/JaniceWuo/MovieRecommend](https://github.com/JaniceWuo/MovieRecommend)
* [https://github.com/zhengyizoey/watchfilms_django_website](https://github.com/zhengyizoey/watchfilms_django_website)
* [刘江的Django教程](https://www.liujiangblog.com/)

### 环境

* Python3.7
* Django2.0
* mysql
* bootstrap

###  实现细节

#### 注册登陆界面

简易的注册登陆界面，分为注册和登陆两个部分，注册需要输入用户名和密码，注册登陆之后进入电影展示页面。

具体内容可随便参考

#### 电影展示界面

电影展示界面需要为电影提供图片，名称，简介，并且提供是否观看过按键。(忽略分类，仅提供简单的电影展示)

暂时不为电影评分，而是简单的看过与未看过两个选择。

具体的界面可参考[https://github.com/zhengyizoey/watchfilms_django_website](https://github.com/zhengyizoey/watchfilms_django_website)

难点可能在于如何存储电影信息，包括图片，简介等。

#### 为我推荐界面

这一模块使用协同过滤算法为用户推荐电影。

提供简单的推荐按键

#### 我的观影清单

为用户展示被选择的观看过的电影。

