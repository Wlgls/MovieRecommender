from django.shortcuts import render,render_to_response, redirect
from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
from login import forms
from . import models
from login.models import Users
from django.forms.models import model_to_dict
from util.Recommend import RunRec, RunRec_by_init


def index(request):
    if not request.session.get("is_login"):
        message = "请先登录"
        login_form = forms.Userform()
        # 这里注意空表单的名字一定不能错，因为前端中已经绑定了login_form这个表单变量名
        return render(request, "login/login.html", locals())
    context = {}
    item_list = dict()
    if request.method == 'GET':
        q = request.GET.get('q')
        if q:  # 如果请求搜索，返回模糊搜索出的电影
           
            current_cat = '查询结果"{}"'.format(q)
            item_list = models.Movies.objects.filter(MovieTitle__icontains = q)
           
        else:  # 如果都没有，就是访问所有电影
            # 该逻辑似乎并没有实现？？？
            item_list = models.Movies.objects.all()
            current_cat= '所有电影'
    # return render(request, 'Items/base.html', locals())
    return render_to_response('Items/index.html',locals())


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
    Username = request.session.get('username')
    UserID = Users.objects.get(Username=Username).UserID
    
    rating = models.Ratings.objects.all()
    if len(rating) < 100:
        # 如果观影人数小于100,就暂时使用默认相关性
        message = ["基于原始的电影之间的关系，我们为你推荐了:"]
        userf = models.Ratings.objects.filter(User=Users.objects.get(pk=UserID))
        userf = [item.Movie.MovieID for item in userf]
        rec = RunRec_by_init(userf)
        item_list = [models.Movies.objects.filter(MovieID__in=rec)]

    else:
        # 如果其中的记录数超过100个，那么我们就可以使用用户自己选择的电影来处理
        message = ["根据电影相似度，我们为你推荐了:", "根据用户相似度，我们为你推荐了:"]
        rating = [[item.User.UserID, item.Movie.MovieID, 1] for item in rating]
        rec1, rec2 = RunRec(UserID, rating)
        item_list = [models.Movies.objects.filter(MovieID__in=rec1), models.Movies.objects.filter(MovieID__in=rec2)]
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
