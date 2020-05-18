from django.shortcuts import render
from django.http import HttpResponse
from . import forms, models
# from sqlalchemy.orm import sessionmaker
from .models import Users# , engine
from django.shortcuts import redirect
from Items.views import index as nextapp
# Create your views here.

# DBsession = sessionmaker(bind=engine)


def register(request):
    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            if password1 != password2:
                message = "两次密码不一致"
                return render(request, "login/register.html", locals())
            else:
                try:
                    same_name_user = Users.objects.get(Username==username)
                    if same_name_user:
                        message = "该用户已存在"
                        return render(request, "login/register.html", locals())
                except:
                    new_user = Users(Username=username, Password=password1)
                    new_user.save()
                    # return redirect("login")
                    return redirect("/login/")
        else:
            message = "请检查数据有效性"
            return render(request, "login/register.html", locals())
    register_form = forms.RegisterForm()
    return render(request, "login/register.html", locals())


def login(request):
    # session = DBsession()
    if request.method == "POST":
        login_form = forms.Userform(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            try:
                user = Users.objects.get(Username=username)
                # session.close()
                print(user)
            except:
                message = "该用户不存在"  # 这个异常是指查询数据库的异常或者当所查对象不再库中也是异常
                return render(request, "login/login.html", locals())  # local()返回所有本地变量，并作为字典类型变量返回
#               正因为返回了login_form变量所以才能让用户在出错的时候能继续填表且不丢失之前填过的数据。
            if password == user.Password:
                return redirect(transform)
            else:
                message = "密码不正确"
                return render(request, "login/login.html", locals())
        else:
            message = "请检查信息是否写正确"
            return render(request, "login/login.html", locals())
    login_form = forms.Userform()  # 如果不是POST请求的话，则返回一个空表来让客户继续填
    return render(request, "login/login.html", locals())


def transform(request):
    return redirect(nextapp)
    # return HttpResponse("这是下一个app的界面")
