from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from SwayamSeva.models import UserDetails, CompleteUserDetails
from SwayamSeva.IndirectUseFiles.aValidate import Validate


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=12, help_text='Required. Enter a valid Aadhaar', label='Aadhaar')
    email = forms.CharField(max_length=127, help_text='Required. Enter a valid Email')

    class Meta:
        model = UserDetails
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_username(self):
        if not Validate(self.cleaned_data['username']):
            raise forms.ValidationError('Invalid Aadhaar Number')
        return self.cleaned_data['username']

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=12, help_text='Required', label='Aadhaar')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = UserDetails
        fields = ('username', 'password')

    def clean(self):
        aadhaar = self.cleaned_data['username']
        password = self.cleaned_data['password']
        '''if not Validate(aadhaar):
            raise forms.ValidationError('Invalid Aadhaar Number')'''
        if not authenticate(username=aadhaar, password=password):
            raise forms.ValidationError('Invalid Aadhaar or Password')


class ApplicationForm(forms.ModelForm):
    Aadhaar = forms.CharField(max_length=12, disabled=True)
    F_name = forms.CharField(max_length=50, disabled=True, label='First Name')
    M_name = forms.CharField(max_length=50, required=False, label='Middle Name')
    L_name = forms.CharField(max_length=50, disabled=True, label='Last Name')
    DOB = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = CompleteUserDetails
        fields = '__all__'

    def clean_Aadhaar(self):
        aadhaar = self.cleaned_data['Aadhaar']
        user = UserDetails.objects.get(username=aadhaar)
        return user