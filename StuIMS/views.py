# Create your views here.

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from stu_db.models import Stu_Info, Admin_info
from django.db import connection
import pymysql


# 视图是一个函数
# 必须传入一个参数 request 请求对象
# def index(request):
#     return HttpResponse('hello')

# 登录页面
def login(request):
    # 判断用户名和密码是否正确
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        m = 0
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        info = Admin_info.objects.all()
        for i in info:
            if i.admin_user != user:
                continue
            else:
                m = 1
        if m == 1:
            for i in info:
                if i.admin_pwd == pwd:
                    m = 2
                    return redirect(admin)
                else:
                    m = 0
                    continue
        if m == 0:
            # 参数1是请求对象request，参数2是需要返回的html页面，参数3需要传入模板的数据
            return render(request, 'login.html', {'error': '用户名或者密码错误'})


# 后台页面
def admin(request):
    # 获取信息表
    if request.method == "GET":
        item = Stu_Info.objects.all()
        # 主页信息
        # 管理员ID
        admin_id = Admin_info.objects.values('id').first()
        # 管理员姓名
        admin_name = Admin_info.objects.values('admin_name').first()
        # 获取学生总数
        stu_sum = 0
        for i in item:
            if i.id:
                stu_sum += 1
        # 查询小于18岁的学生数
        stu_age = 0
        for i in item:
            if i.Stu_age < 18:
                stu_age = stu_age + 1
        return render(request, 'admin.html', locals())
    else:
        a = request.POST.get('sub')
        # print(a)
        # 增加操作，信息录入
        if a == '提交':
            stu_info = {
                "Stu_name": request.POST.get('name'),
                "Stu_sex": request.POST.get('sex'),
                "Stu_age": request.POST.get('age'),
                "Stu_ID": request.POST.get('ID'),
                "Stu_pro": request.POST.get('pro'),
                'Stu_code': request.POST.get('stu_id'),
                'Stu_place': request.POST.get('place'),
                'Tel_No': request.POST.get('phone'),
                "Email": request.POST.get('email'),
            }
            for key in stu_info:
                if stu_info[key] == '':
                    stu_info[key] = '0'
                elif all_Chinese(stu_info["Stu_code"]) or all_Chinese(stu_info["Stu_ID"]) or all_Chinese(
                        stu_info["Stu_age"]) or all_Chinese(stu_info['Tel_No']) == True:
                    return HttpResponse('<h1 style="text-align:center;">请正确输入<h1>')
            Stu_Info.objects.create(**stu_info)
            item = Stu_Info.objects.all()
            stu_sum = Stu_Info.objects.values('id').last()
            stu_age = 0
            for i in item:
                if i.Stu_age < 18:
                    stu_age = stu_age + 1
            return redirect(admin)
        # 修改功能
        elif a == '确认':
            stu_info = {
                "Stu_name": request.POST.get('name'),
                "Stu_sex": request.POST.get('sex'),
                "Stu_age": request.POST.get('age'),
                "Stu_ID": request.POST.get('ID'),
                "Stu_pro": request.POST.get('pro'),
                'Stu_code': request.POST.get('stu_id'),
                'Stu_place': request.POST.get('place'),
                'Tel_No': request.POST.get('phone'),
                "Email": request.POST.get('email'),
            }
            Fc = request.POST.get('FCode')
            # 判断输入是否为空或数字
            for key in stu_info:
                if all_Chinese(stu_info["Stu_code"]) or all_Chinese(stu_info["Stu_ID"]) or all_Chinese(
                        stu_info["Stu_age"]) or all_Chinese(stu_info['Tel_No']) == True:
                    return HttpResponse('<h1 style="text-align:center;">请正确输入<h1>')
                elif stu_info[key] == '':
                    stu_info[key] = '0'
                    # 修改信息
            # filter为过滤，支持多个参数，update是更新方法，支持多个参数
            Stu_Info.objects.filter(id=Fc).update(**stu_info)
            return redirect(admin)
        # 检索功能
        elif a == '搜索':
            stu_code = request.POST.get('search')
            if all_Chinese(stu_code):
                detail_info = Stu_Info.objects.filter(Stu_name=stu_code).all()
                return render(request, 'detail.html', locals())
            elif stu_code != '':
                detail_info = Stu_Info.objects.filter(Stu_code=stu_code).all()
                return render(request, 'detail.html', locals())
            else:
                detail_info = Stu_Info.objects.all()
                return render(request, 'detail.html', locals())


# 判断字符是否为中文
def all_Chinese(word):
    for ch in word:
        if '\u4e00' <= word <= '\u9fff':
            return True
        return False


# 实现删除功能
def del_stu(request):
    nid = request.GET.get('nid')
    Stu_Info.objects.filter(id=nid).delete()
    return redirect(admin)


# 查询的结果页面
def detail(request):
    nid = request.GET.get('nid')
    stu_info = {
        "Stu_name": request.GET.get('name'),
        "Stu_sex": request.GET.get('sex'),
        "Stu_age": request.GET.get('age'),
        "Stu_ID": request.GET.get('ID'),
        "Stu_pro": request.GET.get('pro'),
        'Stu_code': request.GET.get('stu_id'),
        'Stu_place': request.GET.get('place'),
        'Tel_No': request.GET.get('phone'),
        "Email": request.GET.get('email'),
    }
    print(stu_info)
    return render(request, 'edit.html')
# def edit(request):
#     if request.method == 'GET':
#         nid = request.GET.getlist('nid')
#         global stu_id
#         stu_id = nid[0]
#         print(stu_id)
#         return render(request, 'detail.html')
#     else:

#         Stu_Info.objects.filter(id=nid).update(Stu_name=name, Stu_sex=sex, Stu_age=age, Stu_pro=pro, Stu_code=code,
#                                                Stu_place=place, Tel_No=phone, Email=mail, Stu_ID=SID)
#         print(nid)
#         return redirect(admin)
#         # print(stu_id)
#         # return HttpResponse('...')
