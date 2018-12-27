from django.contrib.auth.models import User
from django.db import models


class UserInfo(models.Model):
    # ForeignKey是sql的外健 on_delete=models.CASCADE意味着当对应的外健被删除 它也会被删除
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # choices是一个二元数组 二元数组的第一个值用来存储 第二个值用来显示
    OTHER = 0
    MALE = 1
    FEMALE = 2
    SEX_CHOICES = (
        (OTHER, "other"),
        (MALE, "male"),
        (FEMALE, "female"),
    )
    sex = models.IntegerField(default=0, choices=SEX_CHOICES)
    birthday = models.DateField(auto_now=True)
