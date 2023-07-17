from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from posts.views import PostRetrieveView,PostListView,PostModelViewSet,CommentModelViewSet, calculator

router = routers.DefaultRouter()
router.register('posts', PostModelViewSet)
router.register('comments', CommentModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),

    path('post/', PostListView.as_view(), name='posts-list'),
    path('post/<int:pk>/', PostRetrieveView.as_view(), name='posts-detail'),

    path('calculator/', calculator, name='calculator'),
]
