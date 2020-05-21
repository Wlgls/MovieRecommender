from django.shortcuts import render
from django.http import HttpResponse
from . import forms, models
# from sqlalchemy.orm import sessionmaker
# from .models import Users, engine
from django.shortcuts import redirect
# Create your views here.
# DBsession = sessionmaker(bind=engine)
import hashlib


def hash_code(s, salt='pwz'):
    sha = hashlib.sha256()
    s += salt
    sha.update(s.encode())
    return sha.hexdigest()



def register(request):
    # session = DBsession()
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
                # same_name_user = session.query(Users).filter(Users.Username==username).one()
                same_name_user = models.Users.objects.filter(Username = username)
                if same_name_user:
                    message = "该用户已存在"
                    return render(request, "login/register.html", locals())
                else:
                    # new_user = Users(Username=username, Password=password1)
                    # session.add(new_user)
                    # session.commit()
                    # session.close()
                    new_user = models.Users()
                    new_user.Username = username
                    new_user.Password = hash_code(password1)
                    new_user.save()
                    # return redirect("login")
                    return redirect("/login/")
        else:
            message = "请检查数据有效性"
            return render(request, "login/register.html", locals())
    register_form = forms.RegisterForm()
    return render(request, "login/register.html", locals())


def login(request):
    if request.session.get('is_login', None):
        # 如果用户已登录，则自动跳转到登出页面
        return redirect("/login/logout")
    # ses = DBsession()
    if request.method == "POST":
        login_form = forms.Userform(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            try:
                # user = ses.query(Users).filter(Users.Username==username).one()
                # ses.close()
                user = models.Users.objects.get(Username = username)
            except:
                message = "该用户不存在"  # 这个异常是指查询数据库的异常或者当所查对象不再库中也是异常
                return render(request, "login/login.html", locals())  # local()返回所有本地变量，并作为字典类型变量返回
#               正因为返回了login_form变量所以才能让用户在出错的时候能继续填表且不丢失之前填过的数据。
            if hash_code(password) == user.Password:
                request.session['is_login'] = True
                request.session['username'] = user.Username
                request.session['password'] = user.Password
                return redirect(index)
            else:
                message = "密码不正确"
                return render(request, "login/login.html", locals())
        else:
            message = "请检查信息是否写正确"
            return render(request, "login/login.html", locals())
    login_form = forms.Userform()  # 如果不是POST请求的话，则返回一个空表来让客户继续填
    return render(request, "login/login.html", locals())


def logout(request):
    if not request.session.get('is_login'):
        # 本身就处于未登录状态
        # message = "请先登录！"
        return redirect("/login/")
    # request.session.flush()
    return render(request, "login/logout.html")  # 如果你能见到logout这个界面说明session中的登录状态已经被清除了，不可能再回到之前index了


def confirm_out(request):
    if not request.session.get('is_login'):
        return redirect("/login/")
    request.session.flush()
    return redirect("/login/")


def index(request):
    if not request.session.get("is_login"):
        message = "请先登录"
        login_form = forms.Userform()
        # 这里注意空表单的名字一定不能错，因为前端中已经绑定了login_form这个表单变量名
        return render(request, "login/login.html", locals())
    return render(request, "login/index.html")
