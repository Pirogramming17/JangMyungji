from django.forms import ModelForm
from idea_list.models import Post_dev
from django.utils.translation import gettext_lazy as _


class PostForm(ModelForm):
    class Meta:
        model = Post_dev
        fields = ['devtool_name', 'devtool_kind', 'kind']
        labels = {
            'devtool_name' : _('개발 툴 명'),
            'devtool_kind' : _('개발 툴 종류'),
            'devtool_content' : _('개발 툴 설명'),
        }