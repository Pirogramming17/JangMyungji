from unicodedata import name
from django.db import models

class Post_dev(models.Model):
    devtool_name = models.CharField(max_length=50) #개발툴
    devtool_kind = models.CharField(max_length=50) #종류
    devtool_content = models.TextField() #설명

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'[{self.pk}] {self.devtool_name}'# 타이틀 맞음? 데브써야하는거 아님?

    def get_absolute_url(self):
        return f'/idea_list/{self.pk}/' #포스팅할때 히스토리 옆에 뷰온 사이트 나옴(디테일 페이지로 연결)