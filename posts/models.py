from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

#인스타그램 게시글 모델링
#이미지-조회수-작성자-내용-날짜
class Post(models.Model):
    image = models.ImageField(verbose_name='이미지', null=True, blank=True)
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    view_count = models.IntegerField(verbose_name='조회수', default=0, null=True)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)



#댓글모델
#내용, 작성일 , 게시글, 작성자
class Comment(models.Model):
    Co_content = models.TextField(verbose_name='댓글내용')
    Co_created_at = models.DateTimeField(verbose_name='댓글작성일', auto_now_add=True)
    Co_post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    Co_writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    

