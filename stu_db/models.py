from django.db import models

objects = models.Manager()


# Create your models here.


# 模型类 对应一张数据表
# 管理员信息
class Admin_info(models.Model):
    # max_length最大长度，字符串类型必须定义
    # 管理员id
    # 管理员名字
    admin_name = models.CharField(max_length=20)
    # 管理员账号
    admin_user = models.CharField(max_length=16,default=None)
    # 管理员密码
    admin_pwd = models.CharField(max_length=16,default=None)


class Stu_Info(models.Model):

    # 学生姓名
    Stu_name = models.CharField(max_length=20)
    # 学生性别
    Stu_sex = models.CharField(max_length=10)
    # 身份证号
    Stu_ID = models.BigIntegerField(default=0)
    # 所属专业
    Stu_pro = models.CharField(max_length=30)
    # 学籍号
    Stu_code = models.BigIntegerField(default=0)
    # 手机号码
    Tel_No = models.BigIntegerField(default=0)
    # 电子邮箱
    Email = models.CharField(max_length=40)
    # 学生年龄
    Stu_age = models.IntegerField(default=0)
    # 学生籍贯
    Stu_place = models.CharField(max_length=25)
