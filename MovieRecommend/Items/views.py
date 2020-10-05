# -*- encoding: utf-8 -*-
'''
@File    :   views.py
@Time    :   2020/05/20 16:04:21
@Author  :   王强和张聪
@Version :   1.0: 实现了电影罗列功能(张聪)
@Version :   1.1: 实现了电影推荐视图(王强)
@Version :   2.0: 添加了部分功能(彭友)
@Contact :   smithguazi@gmail.com
'''


from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
from login import forms
from . import models
from login.models import Users
from django.forms.models import model_to_dict
from util.Recommend import RunRec
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random

def index(request):
    """
    电影展示界面的视图函数
    """
    if not request.session.get("is_login"):
        message = "请先登录"
        login_form = forms.Userform()
        # 这里注意空表单的名字一定不能错，因为前端中已经绑定了login_form这个表单变量名
        return render(request, "login/login.html", locals())

    if request.method == 'GET':
        q = request.GET.get('q')
        if q:  # 如果请求搜索，返回模糊搜索出的电影
            current_cat = '查询结果"{}"'.format(q)
            item_list = models.Movies.objects.filter(MovieTitle__icontains = q)
        else:  # 如果都没有，就是访问所有电影
            tmp = models.Movies.objects.all()
            paginator = Paginator(tmp, 4)
            page = request.GET.get('page')
            try:
                item_list = paginator.page(page)
            except PageNotAnInteger:
                # 如果请求的页数不是整数，返回第一页。
                item_list = paginator.page(1)
            except EmptyPage:
                # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
                item_list = paginator.page(paginator.num_pages)
            current_cat= '所有电影'
    # return render(request, 'Items/base.html', locals())
    return render(request, 'Items/index.html',locals())
    
def mylist(request):
    if not request.session.get("is_login"):
        message = "请先登录"
        login_form = forms.Userform()
        # 这里注意空表单的名字一定不能错，因为前端中已经绑定了login_form这个表单变量名
        return render(request, "login/login.html", locals())
    # item_list = list()
    username=request.session.get("username")
    now_user=Users.objects.get(Username=username)
    ratings=models.Ratings.objects.filter(User=now_user)
    if ratings.exists():
        seen_movie=[]
        for rating in ratings:
            seen_movie.append(rating.Movie)
        item_list=seen_movie
        # print(item_list)
    # movies=list(seen_movie)
    # 返回的是queryset，此时并没有立刻执行sql语句
    # get方法返回对象，filter方法返回对象组成的列表
    else:
        message="还没有添加已看过的电影呢"
    return render(request, 'Items/mylist.html', locals())


def recommend(request):
    if not request.session.get("is_login"):
        message = "请先登录"
        login_form = forms.Userform()
        # 这里注意空表单的名字一定不能错，因为前端中已经绑定了login_form这个表单变量名
        return render(request, "login/login.html", locals())
    UserID = request.session.get('userid')


    len_movies = len(models.Movies.objects.all())

    rating = models.Ratings.objects.all()
    User_Seen = [item.Movie for item in rating]
    if len(rating) < 100 or len(set(models.Ratings.objects.values_list('User')))<6:
        # 如果观影人数小于100,就暂时使用默认相关性, 或者人数小于5
        message = ["由于系统中样本数过少，我们为你随即推荐了五部电影:"]
        count = 0
        item_list = [[]]
        while(True):
            random_index = random.randint(0, len_movies)
            temp = models.Movies.objects.get(pk=random_index)
            if temp not in User_Seen:   
                # 去除已经看过的电影
                count += 1
                item_list[0].append(temp)
            if count == 5:
                break

    else:
        # 如果其中的记录数超过100个，那么我们就可以使用用户自己选择的电影来处理
        message = ["根据电影相似度，我们为你推荐了:", "根据用户相似度，我们为你推荐了:"]
        if len(models.Recommend.objects.filter(User=Users.objects.get(pk=UserID))) == 0:
            rating = [[item.User.UserID, item.Movie.MovieID, 1] for item in rating]
            rec1, rec2 = RunRec(UserID, rating)
            item_list = [models.Movies.objects.filter(MovieID__in=rec1), models.Movies.objects.filter(MovieID__in=rec2)]
            for i, mes in enumerate(['item', 'user']):
                for m in item_list[i]:
                    models.Recommend.objects.create(User=Users.objects.get(pk=UserID), Movie=m, kind=mes)
        
        else:
            temp = models.Recommend.objects.filter(User=Users.objects.get(pk=UserID))
            item_list = [[m for m in temp if m.kind=='item'], [m for m in temp if m.kind=='user']]
    toHtml = zip(message, item_list)
    return render(request, 'Items/recommend.html', locals())
    #return render(request, 'Items/index.html', locals())


def add(request):
    if not request.session.get("is_login"):
        message = "请先登录"
        login_form = forms.Userform()
        # 这里注意空表单的名字一定不能错，因为前端中已经绑定了login_form这个表单变量名
        return render(request, "login/login.html", locals())
    new_rating=models.Ratings()
    username=request.session.get('username')
    movieid=request.GET["movieid"]
    get_movie=models.Movies.objects.get(MovieID=movieid)
    get_user=Users.objects.get(Username=username)
    if not models.Ratings.objects.filter(User=get_user, Movie=get_movie) :
        # get()会抛异常，filter不会抛异常
        new_rating.User=get_user
        new_rating.Movie=get_movie
        new_rating.save()
    else:
        message = "已经添加过该电影了"
    return render(request, "Items/exist.html", locals())
