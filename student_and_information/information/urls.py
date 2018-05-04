from django.conf.urls import url

from information import views

urlpatterns = [
    url(r'addinfo',views.addInfo)
]