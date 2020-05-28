import pandas as pd
import numpy as np 


class ItemBasedCF(object):
    def __init__(self, n_rec=5):
        self.moiveSim = None
        self.n_rec = n_rec

    def ComputeSim(self, data, normalization=True):
        """ 
        已知我们的用户user-movie矩阵，求电影相似度
        使用cosine相似度, 公式为:
        cosine = (x1*x2.T)/(sqrt(|x1|)*sqrt(|x2|))
        需要注意的是因为cosine相似度对数值不敏感，仅对方向敏感，所以，我们做了均值归0化
        """ 
        m, n = data.shape
        # 均值归0化
        data = data - np.mean(data, axis=0)
        # 求得是电影相似度
        tmp = np.dot(data.T, data)## tmp_{ij} = m_{i}.T*m_{j}

        # 先求解范数即sqrt(|x1|), # 每一行是一个电影的范数
        # n * 1
        normmovie = np.linalg.norm(data, axis=0).reshape((-1, 1))       
        tmpnorm = np.dot(normmovie, normmovie.T)# np.dot(n*1, 1*n) = n*n
        # 其中tmpnorm_{ij} = sqrt(|xi|)*sqrt(|xj|)
        tmpnorm[tmpnorm==0] = 1e-16# 因为提供的可能是部分电脑，
        # 所以，可能存在有的电影没有被任何人看的可能性，即为0的可能性。防止除法出错

        movieSim = tmp / tmpnorm
        if normalization:
            # 如果需要标准化
            movieSim = 0.5+0.5*movieSim
        self.moiveSim = movieSim
        return movieSim

    def predict(self, userf):
        """ userf: user的选择向量 
        """
        # dot(m*n, n*n)
        tmp = self.moiveSim
        yfit = np.dot(userf, tmp)
        
        # 因为每一个用户对电影的评分是不一样的，为了将其值设置去见一致，我们将其max-min归一化
        interval = np.max(yfit) - np.min(yfit)
        yfit = (yfit - np.min(yfit)) / interval
        return yfit

    def recommend(self, userf):
        yfit = self.predict(userf)
        userf = -1 * (userf-1)
        yfit = userf * yfit# 将看过的电影置为0,在排序中排除
        MovieID = np.argsort(yfit)[::-1][:self.n_rec]
        
        return MovieID

    def costErr(self, userf):
        # 重复率, 即，推荐中有几个是已被看过的
        MovieID = self.recommend(userf)

        return np.sum(userf[MovieID])/self.n_rec


class UserBasedCF(object):
    def __init__(self, n_rec=5):
        self.UserSim = None
        self.n_rec = 5
        self.UserMovie = None

    def ComputeSim(self, data, normalization=True):
        """ 
        已知我们的用户user-movie矩阵，求电影相似度
        使用cosine相似度, 公式为:
        cosine = (x1*x2.T)/(sqrt(|x1|)*sqrt(|x2|))
        需要注意的是因为cosine相似度对数值不敏感，仅对方向敏感，所以，我们做了均值归0化
        """ 
        self.UserMovie = data
        m, n = data.shape
        # 均值归0化
        data = data - np.mean(data, axis=0)
        # 求得是电影相似度
        tmp = np.dot(data, data.T)## tmp_{ij} = m_{i}.T*m_{j}

        # 先求解范数即sqrt(|x1|), # 每一行是一个电影的范数
        # n * 1
        normuser = np.linalg.norm(data, axis=0).reshape((-1, 1))       
        tmpnorm = np.dot(normuser.T, normuser)# np.dot(n*1, 1*n) = n*n
        # 其中tmpnorm_{ij} = sqrt(|xi|)*sqrt(|xj|)
        tmpnorm[tmpnorm==0] = 1e-16# 因为提供的可能是部分电脑，
        # 所以，可能存在有的电影没有被任何人看的可能性，即为0的可能性。防止除法出错

        UserSim = tmp / tmpnorm
        if normalization:
            # 如果需要标准化
            UserSim = 0.5+0.5*UserSim
        self.UserSim = UserSim
        return UserSim

    def recommend(self, userid, userf):
        """ userid: 用户id 
        """
        # dot(m*n, n*n)
        simu = np.argsort(self.UserSim[userid])[::-1][:self.n_rec]
        can_movies = np.sum(self.UserMovie[simu], axis=0)
        userf = -1 * (userf - 1)# 看过的置为0，未看过的置为1
        can_movies = can_movies * userf # 将看过的电影置为0,在排序中排除
        MovieID = np.argsort(can_movies)[::-1][:self.n_rec]

        return MovieID


    def costErr(self, userid):
        # 重复率, 即，推荐中有几个是已被看过的
        MovieID = self.predict(userid)

        return np.sum(self.UserMovie[userid, MovieID])/self.n_rec


def RunRec_by_init(userf):
    # print(userf)
    tmp = pd.read_table('util/ratings.dat',sep='::', header=None,
                     names=['userid', 'movieid', 'score', 'timestamp'], engine='python')

    data = tmp.pivot_table(index='userid', columns='movieid', values='score')
    data = data.fillna(0)
    data[data<3] = 0
    data[data>=3] = 1
    data = data.values
    data = data[:, :967]
    model = ItemBasedCF()

    model.ComputeSim(data)

    tmp = np.zeros(data.shape[1])
    tmp[userf] = 1

    items = model.recommend(tmp)

    return items

def RunRec(userid, Rating):
    rating = pd.DataFrame(Rating)
    movieIDs = np.unique(rating[1])  # 电影ID映射

    data = rating.pivot_table(index=0, columns=1, values=2)
    data = data.fillna(0)
    data = data.values

    userf = data[userid]
    model1 = ItemBasedCF()
    model1.ComputeSim(data)
    item1 = model1.recommend(userf) # 基于事务的

    model2 = UserBasedCF()
    model2.ComputeSim(data)
    item2 = model2.recommend(userid, userf) #基于用户的

    # 映射回去
    return movieID[item1], movieIDs[item2]

if __name__ == '__main__':
   # print(RunRec_by_init(1))
   RunRec_by_init()
