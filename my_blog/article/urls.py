# 引入path 
from django.urls import path
# 引入views.py
from . import views
# 正在部署的应用名称
app_name = 'article'

urlpatterns=[
    # path函数将url映射到视图中
    path('article-list/', views.article_list, name='article_list'),
]