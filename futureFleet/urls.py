from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:comic_id>', views.comic, name='comic'),
    path('test', views.test, name='test'),
    path('blog/<int:blog_id>', views.blog, name='blog'),
]
