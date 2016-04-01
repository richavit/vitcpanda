from django import forms
from django.contrib.auth.models import User
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget 
from services.models import Service

class ServiceForm(forms.Form):
    title = forms.CharField(
        label='Title', widget=forms.TextInput(attrs={'placeholder': 'Provide service name'})
    )    
    description = forms.CharField(
        label='Description', widget=forms.TextInput(attrs={'placeholder': 'Some details about your service'})
    )     
    duraction = forms.CharField(
        label='Duration', widget=forms.TextInput(attrs={'placeholder': 'Time  schedule of service'})
    )
    zip_Code = forms.CharField(
        label='Zipcode',widget=forms.TextInput(attrs={'placeholder': 'Your area zipcode'})
    )
    docfile = forms.FileField(
        label='Select Service Image'
    )
    address = forms.CharField(
        label='Place', widget=forms.TextInput(attrs={'placeholder': 'place where service offer'})
    )
    expire_date = forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))

    active = forms.BooleanField(
        label='Are you sure to publish'
    )
   
class OfferForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = ('title', 'description', 'active', 'duraction', 'address', 'docfile', 'zip_Code', 'expire_date', )




