import pymysql
import pandas as pd
from sqlalchemy import create_engine


path = '/home/smith/Data/MovieRecommender/data/movies.csv'# 更改路径

df = pd.read_csv(path, usecols=['NAME', 'COVER', 'STORYLINE'])

df.dropna(axis='rows', how='any', inplace=True)
df.columns=['MovieTitle', 'Cover', 'StoryLine']# 去掉所有没有图片，没有简介的电影

config = dict(
    username='smith', password='smith',address='localhost', 
    database='MovieRecommend', charset='utf8'
)   # 更改自己的数据库信息
engine = create_engine("mysql+pymysql://{username}:{password}@{address}/{database}?charset={charset}".format(**config))# 使用自己的用户名和密码
con = engine.connect()
df.to_sql(name='Movies', con=con, if_exists='append', index=False)
