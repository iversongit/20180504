from django.db import models

# Create your models here.
class Student(models.Model):
    s_name = models.CharField(max_length=10)
    s_tel = models.CharField(max_length=11)

    class Meta:
        db_table = "student"

class StudentInfo(models.Model):
    s_addr = models.CharField(max_length=30)
    # ImageField中的_check_image_library_installed方法会导入Pillow包
    # from PIL（即Pillow） import Image
    # 所以使用前先要pip install Pillow
    s_image = models.ImageField(upload_to='upload',null=True) # 把上传的图片文件存在upload文件夹中
    s = models.OneToOneField(Student)

    class Meta:
        db_table = "studentinfo"