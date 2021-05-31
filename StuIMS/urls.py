"""StuIMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from StuIMS import views
from django.contrib.auth.decorators import login_required
import re
# from StuIMS.views import admin.detail

urlpatterns = [
    # 网页url地址
    # 正则表达式匹配链接
    url(r'^login/', views.login),
    url(r'^admin/', views.admin),
    url(r'^del_stu/', views.del_stu),
    url(r'^detail/', views.detail),
]
