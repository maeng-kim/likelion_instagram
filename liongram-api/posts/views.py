from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Post, Comment

from .serializers import (PostBaseModelSerializer,PostListModelSerializer,ModelSerializer, CommentHyperlinkedSerializer, PostRetrieveModelSerializer)

from rest_framework import generics

class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListModelSerializer

class CommentModelViewSet(ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class = CommentHyperlinkedSerializer

#목록
class PostListView(generics.ListAPIView, generics.CreateAPIView):
    queryset=Post.objects.all()
    serializer_class = PostListModelSerializer
#상세
class PostRetrieveView(generics.RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class = PostRetrieveModelSerializer


@api_view()
def calculator(request):
    # 1. 데이터확인
    num1 = request.GET.get('num1', 0)
    num2 = request.GET.get('num2', 0)
    operators = request.GET.get('operators')
    #2. 계산
    if operators == '+':
        result = int(num1)+int(num2)
    elif operators == '-':
        result = int(num1)-int(num2)
    elif operators == '*':
        result = int(num1)*int(num2)
    elif operators == '/':
        result = int(num1)/int(num2)
    else:
        result=0
    data = {
        'type': 'FBV',
        'result': result,
    }
    #3. 응답
    return Response(data)




