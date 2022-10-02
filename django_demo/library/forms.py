from socket import fromshare
from xml.dom import ValidationErr
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profilis, Uzrasas, Kategorija

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    
    def clean_username(self):
        data = self.cleaned_data['username']
        if User.objects.filter(username=data).exists():
            raise ValidationError(f'Vartotojo vardas {data} užimtas!')
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise ValidationError(f'El. paštas {data} užimtas!')
        return data

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        password2 = cleaned_data['password2']
        if password != password2:
            raise ValidationError('Slaptažodžiai nesutampa')

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfilisUpdateForm(forms.ModelForm):
    class Meta:
        model = Profilis
        fields = ['nuotrauka']
'''
class UserUzrasasCreateForm(forms.ModelForm):
    class Meta:
        model = Uzrasas
        fields = ['title', 'kategorija', 'summary', 'cover']
        #widgets = {'uzrasas.id': forms.HiddenInput()}
'''
'''
class UserKategorijaCreateForm(forms.ModelForm):
    class Meta:
        model = Kategorija
        fields = ['first_name', 'description']
        widgets = {'kategorija.id': forms.HiddenInput()}

'''