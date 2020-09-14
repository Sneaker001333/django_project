from django.contrib import admin
# Register your models here.
# 导入ArticlePost模块
from .models import ArticlePost

# 注册articlePost到admin中
admin.site.register(ArticlePost)

