我负责login app设计（windows开发）
1.首先：clone下代码之后需要安装好虚拟环境venv  (目前不知道怎么为clone下来的程序安装虚拟环境？)
2.配置好所需库  ok  --->可以安装anaconda连接到pycharm中作为python环境来辅助编程（继承了很多库以及方便版本管理）
3.连接好个以及完成数据库的建表和app中的models设计人MySQL数据库   windows可以在mysql的my.ini文件中更改开放的端口
                （这里推荐使用linux下的MySQL连接，但是如果是用） 所以我准备试一下在云端的虚拟机上做数据库主机,失败！！！
                找不到原因，错误日志中没有内容？？？why？？？

        我现在pymysql连接数据库部分应该没有问题，只是在应用ORM模块的时候有问题，不能正常翻译成SQL语句

4.设计数据模型models：根据数据库的格式来构造模型
5.根据设计的urls路由搭建视图结构

注：windows下，配置MySQL确实会有许多bug，例如时区问题，还有pymysql模块的使用都需要进行一些debug，详见我的网页收藏夹

有一个问题：就是连接MySQL时，原先有的数据表不会被覆盖吗，所以makemigrations时没有变化？？？

总结一下：连接MySQL时，流程是：先配置好settings.py中的database内容之后，通过任意一种ORM技术实现python语言描述的数据库中的数据结构 即可
总的来讲，就是： python语言  通过  ORM技术(对象关系映射)  变为SQL语句  再通过  数据库驱动   对目标数据库执行SQL语句
                               例：sqlalchemy，DjangoORM               例：pymysql,mysqlconnector,sql_db
                               不同的ORM框架有不同的语法                   数据库驱动本身可以通过内部的游标cursor来操作数据库


 5.13已做好了login与register页面，还需要实现密码的加密存储（HASH）,以及为完善的登录逻辑，以及添加django自带的可视化的后台数据库页面

 首先登录逻辑问题：整体登录页面的逻辑应该是：
                                           1.未登录的用户不允许访问index界面（电影展示界面），访问到时自动跳转登录页面
                                           2.已登录用户不允许再重复登录，除非先登出(即检测到重复登录时，自动跳转登出界面)
                                           3.所以还需要设计一个登出，可能不需要页面，但是要体现注销
                                           4.已登录人员访问register时自动跳转到index页面
                              综上根据需求，我们需要使用session来帮我们存储登录状态！(session中的数据可视为字典类型数据)
                              为什么要用session呢？因为cookie将数据封装在了httprequest中，毫无安全性
                              而session可以将数据封装在服务端，这样不会很轻松地被恶意获取，且我们可以将session数据存放在数据库中
                              session就是与每个httprequest绑定在一起的一个会话，记录着一些数据，这个请求消失时session也消失

其次，我们将数据库用django自带的admin页面显示出来  (已完成)

Python内置的hashlib模块为我们提供了多种安全方便的摘要方法:md5(),sha1(), sha224(), sha256(), sha384(), sha512(), blake2b()，blake2s()，sha3_224(), sha3_256(), sha3_384(), sha3_512(), shake_128(), shake_256()
使用样例：
sha256()能创建一个SHA-256对象。然后就可以使用通用的update()方法将bytes类型的数据添加到对象里
最后通过digest()或者hexdigest()方法获得当前的摘要
注意了 update()方法现在只接受bytes类型的数据，不接收str类型。


5.20 计划更改：（改用新的ORM技术）django.db自带的models做模型设计
需要修改的地方是：
1.将models.py模块的模型设计改为models设计
2.将之前所有需要用sqlalchemy做查询的部分换成models的一套语句
3.实现admin的显示    创建后台用户名:admin 密码：py991218

出现新问题，改用models（自带的ORM技术）后，出现连接MySQL数据库密码有误的问题:  解决措施，安装cryptography模块
另外一个问题就是：如何实现主键在删除用户之后重新置数。（可能要写一个事务）

5.21:最后还需要改进的地方：    ！前端设计！需要在确认退出的页面（logout.html）中添加两个button尽量好看