from django. forms import ModelForm
from third.models import Movie
from django.utils.translation import gettext_lazy as _
class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'year', 'genre', 'point', 'running_time', 'review', 'producer', 'actor']
        labels = {
            'name': _('제목'),
            'year': _('개봉년도'),
            'genre': _('장르'),
            'point': _('별점'),
            'running_time': _('러닝타임'),
            'review': _('리뷰'),
            'producer': _('감독'),
            'actor': _('배우')
        }
