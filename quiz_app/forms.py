from django.forms import ModelForm
from . import models

class UserForm(ModelForm):
    class Meta:
        model = models.User
        fields = ["name","style1","style2","style3","artist","mood","linked_track"]
