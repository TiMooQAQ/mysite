from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('regist/', views.regist, name='regist'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('blog_list/', views.blog_list, name='blog_list'),
    path('blog_detail/<str:id>', views.blog_detail, name='blog_detail'),
]
