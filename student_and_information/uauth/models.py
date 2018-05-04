from django.db import models

# Create your models here.
class User(models.Model):
    u_name = models.CharField(max_length=10)
    u_password = models.CharField(max_length=255)
    u_ticket = models.CharField(max_length=30,null=True)

    class Meta:
        db_table = "user"

class RequestCount(models.Model):
    c_path_name = models.CharField(max_length=20,null=True)
    c_path_count = models.IntegerField(default=0)
    # c_addstu = models.IntegerField(default=0)
    # c_login = models.IntegerField(default=0)
    # c_logout = models.IntegerField(default=0)
    class Meta:
        db_table = "request_count"