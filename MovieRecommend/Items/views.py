from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from . import models
from django.forms.models import model_to_dict


def index(request):
    context = {}
    item_list = dict()
    if request.method == 'GET':
        q = request.GET.get('q')
        if q:  # 如果请求搜索，返回模糊搜索出的电影
           
            current_cat = '查询结果"{}"'.format(q)
            item_list = models.Movies.objects.filter(MovieTitle__icontains = q)
           
        else:  # 如果都没有，就是访问所有电影
            
            item_list = models.Movies.objects.all()
            current_cat= '所有电影'
    #return render(request, 'Items/index.html',context)
    return render_to_response('Items/index.html',locals())

