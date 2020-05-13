我负责login app设计（windows开发）
1.首先：clone下代码之后需要安装好虚拟环境venv  (目前不知道怎么为clone下来的程序安装虚拟环境？)
2.配置好所需库  ok  --->可以安装anaconda连接到pycharm中作为python环境来辅助编程（继承了很多库以及方便版本管理）
3.连接好个以及完成数据库的建表和app中的models设计人MySQL数据库   windows可以在mysql的my.ini文件中更改开放的端口
                （这里推荐使用linux下的MySQL连接，但是如果是用） 所以我准备试一下在云端的虚拟机上做数据库主机,失败！！！
                找不到原因，错误日志中没有内容？？？why？？？

        我现在pymysql连接数据库部分应该没有问题，只是在应用ORM模块的时候有问题，不能正常翻译成SQL语句

4.设计数据模型models：根据数据库的格式来构造模型
5.根据设计的urls路由搭建视图结构


5.13已做好了login与register页面，还需要实现密码的加密存储（HASH），邮箱验证功能。

有一个问题：就是连接MySQL时，原先有的数据表不会被覆盖吗，所以makemigrations时没有变化？？？

总结一下：连接MySQL时，流程是：先配置好settings.py中的database内容之后，通过任意一种ORM技术实现python语言描述的数据库中的数据结构 即可
总的来讲，就是： python语言  通过  ORM技术(对象关系映射)  变为SQL语句  再通过  数据库驱动   对目标数据库执行SQL语句
                               例：sqlalchemy，DjangoORM               例：pymysql,mysqlconnector,sql_db
                               不同的ORM框架有不同的语法                   数据库驱动本身可以通过内部的游标cursor来操作数据库