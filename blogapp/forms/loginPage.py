from django.forms import ModelForm
from ..models.user.user import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        # exclude = ['host']