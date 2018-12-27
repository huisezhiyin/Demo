from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http.response import HttpResponseRedirect
from django.contrib.auth import logout


class UserViewSet(GenericViewSet):

    # 注册，post方法
    @action(methods=["POST"], detail=False)
    def register(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        # username和password不能缺失 否则无法注册 返回http code 400
        if not username or not password:
            return Response(status=400,
                            data={"msg": "need username or password"})
        # username已存在 返回http code 409
        if User.objects.filter(username=username):
            return Response(status=409, data={"msg": "username existed"})
        # 使用user的create_user方法创建用户 注意：尽量用此方法创建用户
        user = User.objects.create_user(
            username=username,
            password=password)
        return Response({"msg": "success"})

    # 登录，post方法
    @action(methods=["POST"], detail=False)
    def login(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            return Response(status=400,
                            data={"msg": "need username or password"})
        # django官方的密码验证 验证密码务必使用此函数
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # django的官方用户登录函数 登录用户使用此函数
            login(request, user)
            # 跳转到info页面
            return HttpResponseRedirect("/user/info")
        else:
            # 密码或账号错误 返回403错误
            return Response(status=403,
                            data={"msg": "username or password error"})

    # 登出，get方法(这里是为了图方便，其实应该使用put/post方法)
    @action(methods=["GET"], detail=False)
    def logout(self, request, *args, **kwargs):
        logout(request)
        # 重定向至home
        return HttpResponseRedirect("/hello/world")

    @action(methods=["GET"], detail=True)
    def info(self, request, *args, **kwargs):
        # django中常用的获取当前用户的方法
        user = request.user
        # 目前暂时没有做info的详细 可以只返回一个id
        return Response({"user_id":user.id})

