from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room

        # to render all, else we can use list to specify what fields we want
        fields = '__all__'

        #to hide the host and participants from the form fields

        exclude = ['host', 'participants']
         