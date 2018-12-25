from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response


class HelloWorldViewSet(GenericViewSet):

    @action(detail=False)
    def world(self, request, *args, **kwargs):
        return Response({"code": 0, "msg": "hello world!"})
