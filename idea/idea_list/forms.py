from django.forms import ModelForm
from idea_list.models import Post
from django.utils.translation import gettext_lazy as _


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'head_image', 'interest', 'devtool']
        labels = {
            'title' : _('아이디어명'),
            'content' : _('아이디어 설명'),
            'head_image' : _('IMAGE'),
            'interest' : _('아이디어 관심도'),
            'devtool' : _('예상 개발툴'),
        }