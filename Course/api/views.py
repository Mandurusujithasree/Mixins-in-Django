from django.shortcuts import render
from api.models import Course
from rest_framework.response import Response
from api.serializers import CourseSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics,mixins
# Create your views here.

class Course_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
    
class Course_detail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    def get(self,request,pk):
        return self.retrieve(request,pk)
    def post(self,request,pk):
        return self.update(request,pk)
    def delete(self,request,pk):
        return self.destroy(request,pk)