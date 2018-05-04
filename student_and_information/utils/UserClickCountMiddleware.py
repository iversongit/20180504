from django.utils.deprecation import MiddlewareMixin

from uauth.models import RequestCount

import logging
logger = logging.getLogger('auth')
class ClickCountMiddleware(MiddlewareMixin):
    def process_request(self,request):
        # 统计访问的url以及次数
        path = request.path
        try:
            rc = RequestCount.objects.get(c_path_name=path)
            if rc:
                rc.c_path_count += 1
                rc.save()
        except Exception as e:
            # print(e)
            logger.error(e)
            RequestCount.objects.create(
                c_path_name=path,
                c_path_count=1
            )
        # if request.path == '/uauth/login/' and request.method == "POST":
        #     clickEvent = RequestCount.objects.get(c_path_name='c_login')
        #     clickEvent.c_path_count += 1
        #     clickEvent.save()
        # elif request.path == '/uauth/logout/' and request.method == "GET" :
        #     clickEvent = RequestCount.objects.get(c_path_name='c_logout')
        #     clickEvent.c_path_count += 1
        #     clickEvent.save()
        # elif request.path == '/stuapp/addstu/' and request.method == "POST":
        #     clickEvent = RequestCount.objects.get(c_path_name='c_addstu')
        #     clickEvent.c_path_count += 1
        #     clickEvent.save()