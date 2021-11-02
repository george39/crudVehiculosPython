from django.forms import ModelForm
from mainapp.models import Vehicle



class FormVehicle(ModelForm):

    class Meta:
        model = Vehicle
        fields = '__all__'

