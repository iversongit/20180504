from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from student import views
from rest_framework.routers import SimpleRouter
router = SimpleRouter()  # 定义一个路由
router.register(r'student',views.StudentEdit) # studentEdit -- 类名

urlpatterns = [
    url(r'^addstu/',views.addStu,name='add'),
    url(r'^index/',login_required(views.index),name='index'),# 返回所有学生信息(必须要登录才能访问)
    url(r'^stupage/',views.stuPage),
    url(r'^addstuinfo/(?P<stu_id>\d+)',views.addStuInfo,name="addinfo"),
    url(r'^showstu/',views.showStu)
]

urlpatterns += router.urls  # 将路径与对应的方法添加到urlpatterns中