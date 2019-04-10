from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
# from django.contrib.auth.models import User
from .serializer import TestModelSerializer
from .models import TestModel
from rest_framework import mixins
from rest_framework import generics


# class TestModelDetail(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = TestModel.objects.all()
#     serializer_class = TestModelSerializer

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
class TestModelDetail(generics.RetrieveUpdateDestroyAPIView,generics.ListCreateAPIView):
    queryset=TestModel.objects.all()
    serializer_class=TestModelSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)