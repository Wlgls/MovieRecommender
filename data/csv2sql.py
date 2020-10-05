import pymysql
import pandas as pd
from sqlalchemy import create_engine

# csv存储到sql中
path = 'movies.csv'# 更改路径

df = pd.read_csv(path, usecols=['电影名称', '海报', 'summary', '链接', '评分'])

df.dropna(axis='rows', how='any', inplace=True)
df.columns=['MovieTitle', 'grade', 'DoubanLink','Cover', 'StoryLine']

config = dict(
    username='*****', password='*****',address='localhost', 
    database='MovieRecommend', charset='utf8'
)   # 更改自己的数据库信息
engine = create_engine("mysql+pymysql://{username}:{password}@{address}/{database}?charset={charset}".format(**config))# 使用自己的用户名和密码
con = engine.connect()
df.to_sql(name='Movies', con=con, if_exists='append', index=False)
