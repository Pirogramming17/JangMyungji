from random import choices
from secrets import choice
from django.db import models


class Post(models.Model):
    DEVTOOL_CHOICES = {
    ('Node.js', 'Node.js'),
    ('Django', 'Django'),
    ('C++', 'C++'),
    ('Java', 'Java'),
    ('React', 'React'),
    ('Spring', 'Spring'),
    ('not-specified', 'Not Specified')
  }


    title = models.CharField(max_length=50) #아이디어명
    content = models.TextField() #설명
    head_image = models.ImageField(upload_to = 'idea_list/images/%Y/%m/%d/', blank=True)#이미지 파일

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    interest = models.PositiveIntegerField(default=0) #관심도(number)
    devtool = models.CharField(max_length=80, choices=DEVTOOL_CHOICES, null=True)#개발툴(셀렉박스)

    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'/idea_list/{self.pk}/' #포스팅할때 히스토리 옆에 뷰온 사이트 나옴(디테일 페이지로 연결)