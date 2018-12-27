from django.contrib.auth.models import User
from django.db import models


class UserInfo(models.Model):
    # ForeignKey是sql的外健 on_delete=models.CASCADE意味着当对应的外健被删除 它也会被删除
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # choices是一个二元数组 二元数组的第一个值用来存储 第二个值用来显示
    SEX_CHOICES = (
        (0, "other"),
        (1, "male"),
        (2, "female"),
    )
    sex = models.IntegerField(default=0, choices=SEX_CHOICES)
    brith = models.DateField(auto_now=True)
