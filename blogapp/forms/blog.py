from django.forms import ModelForm
from ..models.blog.blog import Blog

class blogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'subtitle', 'post', 'user')
        exclude = ['user']