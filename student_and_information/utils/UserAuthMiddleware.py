from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

from uauth.models import User


class AuthMiddleware(MiddlewareMixin):
    def process_request(self,request): # 函数名固定
        # 进行正式逻辑业务处理之前，统一验证登录
        # 如果return none或者不写，则验证成功
        if request.path == '/uauth/login/'or request.path == '/uauth/regist/':
            return None

        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect('/uauth/login/')

        users = User.objects.filter(u_ticket=ticket)
        if not users:
            return HttpResponseRedirect('/uauth/login/')

        request.user = users[0]  #  request.user: 存放当前登录用户的信息,在其他逻辑处理地方
                                 # 便可随时获取该用户信息