from django.db import models


class CommodityCategory(models.Model):
    name = models.CharField(max_length=512)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


class Commodity(models.Model):
    # 商品的名称 最大长度设置为512
    name = models.CharField(max_length=512)
    # 价格 浮点型
    price = models.FloatField(default=0.0)
    # 商品描述 TextField是大文本字段
    description = models.TextField()
    # 商品图片链接 URLField是CharField的升级 默认max_length是200
    image_link = models.URLField(max_length=512)
    # 类别 外健 因为type是python的关键字 尽量不要使用type作为自定义变量名
    # on_delete是当对应的外健被删除时的处理方法 这里选择的是set null
    # 当on_delete是set null时 此字段的null必须可以为空 即null=True
    # 另：如果你在此设置外健字段 已设置的外健字段CommodityCategory最好放在上面而不是下面
    category = models.ForeignKey(
        CommodityCategory, on_delete=models.SET_NULL, null=True)
    # 创建时间 auto_now_add为true 在数据第一次生成时记录当前时间 不会改变
    created_time = models.DateTimeField(auto_now_add=True)
    # 更新时间 auto_now为true 每次此条数据更改时都会更新此字段为当前时间
    updated_time = models.DateTimeField(auto_now=True)
