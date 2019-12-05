from django.forms import ModelForm
from .models import squirrel

class update_squirrel(ModelForm):

    class Meta:
        model = squirrel
        fields = '__all__'


class create_squirrel(ModelForm):

    class Meta:
        model = squirrel
        fields = '__all__'
