## 电影推荐系统

一个简易的电影推荐系统，包括用户注册登陆，展示电影信息，为我推荐电影，我的观影记录四个模块。

### 参考内容

* [https://github.com/zhengyizoey/watchfilms_django_website](https://github.com/zhengyizoey/watchfilms_django_website)
* [刘江的Django教程](https://www.liujiangblog.com/)
* [官方文档](https://docs.djangoproject.com/zh-hans/3.0/)

### 数据来源

爬取豆瓣电影TOP250

### 环境

* Ubuntu(推荐使用)
* Python3.6
* Django2
* mysql
* bootstrap

###  实现细节

#### 注册登陆界面

简易的注册登陆界面，分为注册和登陆两个部分，注册需要输入用户名和密码，注册登陆之后进入电影展示页面。

具体内容可随便参考

#### 电影展示界面

电影展示界面需要为电影提供图片，名称，简介，并且提供是否观看过按键。(忽略分类，仅提供简单的电影展示)

暂时不为电影评分，而是简单的看过与未看过两个选择。

简单的界面可参考[https://github.com/zhengyizoey/watchfilms_django_website](https://github.com/zhengyizoey/watchfilms_django_website)

#### 为我推荐界面

这一模块使用协同过滤算法为用户推荐电影。

提供简单的推荐按键

#### 我的观影清单

为用户展示被选择的观看过的电影。

### 实现过程

#### 大体设计

我们创建三个Apps，这样尽量可以两个Apps并行开发互不干扰。其主要命令为:

```
$: python manage.py startapp login
$: python manage.py startapp Items
```

​	添加并设置了urls.py, views等文件。具体内容可直接参考源码。

#### 创建数据库

数据库使用mysql关系型数据库

约束(便于后期合并, 注意大小写):

* 在本地建立数据库时，数据库名请使用"MovieRecommend"

* 一共有三个表分别为"Users", "Movies", "Rating", "Recommend"。其表结构规定如下(具体在个app的models中):

  | Users | UserID                | Username             | Password       |
  | :---- | --------------------- | -------------------- | -------------- |
  | eg    | 1                     | smith                | guazi          |
  | 说明  | 主键,自增,非空, INT型 | 唯一, 非空，字符串型 | 非空，字符串型 |

  | Movies | MovieID                 | MovieTitle     | Cover                                                  | StoryLine      | DoubanLink | grade |
  | ------ | ----------------------- | -------------- | ------------------------------------------------------ | -------------- | ---------- | ----- |
  |        |                         |                |                                                        |                |            |       |
  | 说明   | 主键，自增，非空，INT型 | 非空，字符串性 | 字符串型(存储电影封面的链接，部分电影无封面，需要处理) | 非空，字符串型 | 字符串性   | 整型  |

  | Rating | ID                      | UserID             | MovieID           |
  | ------ | ----------------------- | ------------------ | ----------------- |
  | eg     | 1                       | 1                  | 1                 |
  | 说明   | 主键，自赠，非空，INT型 | 外键，非空 , INT型 | 外键，非空，INT型 |
  
  | Recommend | ID                 | User               | Movie              | Kind     |
  | --------- | ------------------ | ------------------ | ------------------ | -------- |
  |           | 外键，非空 , INT型 | 外键，非空 , INT型 | 外键，非空 , INT型 | 字符串型 |

创建数据库请设置编码为utf-8

```
CREATE DATABASE MovieRecommend CHARACTER SET utf8 COLLATE utf8_general_ci;
```

不推荐使用root的用户，所以创建一个用户用于远程访问。

```
GRANT ALL PRIVILEGES ON MovieRecommend.* TO smith@"%" IDENTIFIED BY "smith"; 
```

之后在MovieRecommend/settings.py中设置数据库信息:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'MovieRecommend',
        'USER': '*****',
        'PASSWORD': '****',        
        'HOST': '127.0.0.1',
            'PORT': '3306',
    }
}
```

然后运行以下命令建立数据库表

```
python manage.py makemigrations
python manage.py migrate
```

#### 数据预处理

为了更加合适的实现项目，在数据库中首先存储一些数据，其中，数据来源在/data/movies.csv。这些数据已经经过了 处理。只需要将其存入数据库表中即可。

处理数据的代码在csv2sql.py，注意其中数据库的信息自行更改。

现在可以去工作了

#### 工作方式

请直接克隆我的项目，并学习一点点git的格式，当你在设计时，请为自己创建一个单独的分支，而不是直接在master上进行操作提交。





