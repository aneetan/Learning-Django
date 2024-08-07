from django.forms import ModelForm
from .models import Room
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class RoomForm(ModelForm):
    class Meta:
        model = Room

        # to render all, else we can use list to specify what fields we want
        fields = '__all__'

        #to hide the host and participants from the form fields

        exclude = ['host', 'participants']
         

class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
