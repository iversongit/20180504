from django.conf.urls import url
from uauth import views

urlpatterns = [
    url(r'^regist/',views.regist),
    url(r'^login/',views.login),
    url(r'^logout/',views.logout),
    url(r'^requestcount/',views.requestCount),
    url(r'^djlogin/',views.djLogin),
    url(r'^djregist/',views.djRegist),
    url(r'^djlogout/',views.djLogout),
]