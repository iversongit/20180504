from rest_framework import serializers

from student.models import Student


class StudentSerializer(serializers.ModelSerializer):
    s_name = serializers.CharField(  # 自定义错误名称
        error_messages={
            'blank':'用户名不能为空',
            'max_length':'用户名不能超过十个字符'
        },
        max_length=10
    )

    s_tel = serializers.CharField(
        error_messages={
            'blank':'电话不能为空'
        }
    )
    class Meta:
        model = Student
        fields = ['id','s_name','s_tel']

    def to_representation(self, instance): # 将实例序列化
        data = super().to_representation(instance) # 获取每一个学生的信息
        try:
            data['s_addr'] = instance.studentinfo.s_addr
        except Exception as e:
            data['s_addr'] = ""
        return data