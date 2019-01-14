from rest_framework.viewsets import GenericViewSet, ModelViewSet
from app_ex.poseidon.models import Commodity, CommodityCategory
from rest_framework.response import Response


class CommodityViewSet(GenericViewSet, ModelViewSet):
    queryset = Commodity.objects.filter()
    verification_list = ["name", "price", "description", "image_link",
                         "category_id"]

    # 这里使用的是python的多继承 同时继承GenericViewSet类和ModelViewSet类

    # GenericViewSet的主要作用是支撑更复杂的视图类——比如ModelViewSet
    # ModelViewSet也是一个很重要的视图类 他提供了一系列包装后的restful增删改查的接口
    # 注意 接下来对部分函数的重写仅是教程的一部分，不代表自带的函数无法支撑业务
    # 在很多情况下 你不需要更改自带的任何东西 就可以完成restful api接口的构建

    # 重写create方法用来创建新商品
    def create(self, request, *args, **kwargs):
        if not set(self.verification_list).issubset(set(request.data.keys())):
            return Response(status=401, data={"msg": "Missing parameter"})
        # 先查找对应的货品分类是否存在
        try:
            category = CommodityCategory.objects.get(
                id=request.data.get("category_id"))
        except CommodityCategory.DoesNotExist:
            return Response(status=404, data={"msg": "category DoesNotExist"})
        # 注:此处可以采用序列化器来进行数据验证和存储 但是一口吃不成胖子 先讲简单的方法
        # 注2:此处不捕捉异常而是自由抛出 注意 在开发版本这样做是对自己的仁慈
        commodity = Commodity.objects.create(
            name=request.data.get("name"),
            price=request.data.get("price"),
            description=request.data.get("description"),
            image_link=request.data.get("image_link"),
            category=category
        )
        return Response({"code": 0, "commodity_id": commodity.id})

    # 重写list方法用来筛选商品
    def list(self, request, *args, **kwargs):
        # 种类
        category_id = request.data.get("category_id", None)
        # 价格
        price_min = request.data.get("min", None)
        price_max = request.data.get("max", None)
        # 名字 非模糊搜索
        name = request.data.get("name", None)
        queryset = self.queryset
        if category_id:
            category = self.category(category_id)
            if isinstance(category, Response):
                return category
            else:
                queryset = queryset.filter(category=category)
        if price_min:
            queryset = queryset.filter(price__gte=price_min)
        if price_max:
            queryset = queryset.filter(price__lte=price_max)
        if name:
            queryset = queryset.filter(name__icontains=name)
        # 是不是觉得上面的查询特别的浪费口舌 其实django和django rest framework都有快捷方法

        if queryset:
            # values_list方法可以把orm查询出来的数据转换成json
            # 当然如果使用rest framework的方法 就要使用序列化器了
            return Response(
                {"code": 0, "data": queryset.values_list(flat=True)})
        else:
            return Response(status=404, data={"msg": "commodity not found"})

    # 重写retrieve方法来获取单个货物的详情
    def retrieve(self, request, *args, **kwargs):

        pass

    # 重写update方法来对商品进行更新
    def update(self, request, *args, **kwargs):
        pass

    # 重写destroy方法来删除商品
    def destroy(self, request, *args, **kwargs):
        pass

    @staticmethod
    def category(category_id):
        try:
            category = CommodityCategory.objects.get(id=category_id)
        except CommodityCategory.DoesNotExist:
            return Response(status=404, data={"msg": "category DoesNotExist"})
        return category


class CommodityCategoryViewSet(GenericViewSet, ModelViewSet):
    pass
