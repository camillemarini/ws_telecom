from django.forms import ModelForm
from frontapp.models import Probicipant


class ProbicipantForm(ModelForm):
    class Meta:
        model = Probicipant
        fields = '__all__'
