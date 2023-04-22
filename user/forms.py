from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password', 'class':'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm password', 'class':'form-control'}))
    email            = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    name             = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    mobile           = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address          = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['name', 'mobile', 'email','address', 'password']

    
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password     = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('password dose not match !!')
        