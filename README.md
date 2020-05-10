## 电影推荐系统

一个简易的电影推荐系统，包括用户注册登陆，展示电影信息，为我推荐电影，我的观影记录四个模块。

因为实现的时间大概也有十几天，所以大概率会是一个拼凑而成的怪物，大家尽力而为。

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

### 实现过程

#### 2020年5月10日 -- 创建数据库

数据库使用mysql关系型数据库

约束(便于后期合并, 注意大小写):

* 在本地建立数据库时，数据库名请使用"MovieRecommend"

* 一共有三个表分别为"Users", "Movies", "Rating"。其表结构规定如下:

  | Users | UserID                | Username             | Password       |
  | :---- | --------------------- | -------------------- | -------------- |
  | eg    | 1                     | smith                | guazi          |
  | 说明  | 主键,自增,非空, INT型 | 唯一, 非空，字符串型 | 非空，字符串型 |

  | Movies | MovieID                 | MovieTitle     | Cover                                                        | StoryLine                                                    |
  | ------ | ----------------------- | -------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | eg     | 1                       | 太极           | https://img3.doubanio.com/view/photo/s_ratio_poster/public/p1833562883.jpg | 周星驰在片中饰演一名隐姓埋名的太极宗师，他移居美国在唐人街打工洗盘子，为了保护受暴徒威胁的同胞们，他挺身而出，此后创办了武术学校将他的一身好功夫传授给他人。 |
  | 说明   | 主键，自增，非空，INT型 | 非空，字符串性 | 字符串型(存储电影封面的链接，部分电影无封面，需要处理)       | 非空，字符串型                                               |

  | Rating | ID                      | UserID             | MovieID           |
  | ------ | ----------------------- | ------------------ | ----------------- |
  | eg     | 1                       | 1                  | 1                 |
  | 说明   | 主键，自赠，非空，INT型 | 外键，非空 , INT型 | 外键，非空，INT型 |

创建代码如data/file.sql

运行:

```
mysql -uusername -pusername >file.sql
```

如果你是使用root用户创建的数据库，请创建一个新的用户，使用这个新的用户来对database进行访问例如:

```
GRANT ALL PRIVILEGES ON MovieRecommend.* TO smith@"%" IDENTIFIED BY "smith"; 
```

#### 数据预处理

将部分电影数据存入数据库中，数据集为data/movies.csv

运行代码:csv2sql.py（注意更改自己的信息）



 

