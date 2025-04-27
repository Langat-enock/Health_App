# forms.py

from django import forms
from .models import CustomUser, ClientProfile

class ClientRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    contact = forms.CharField(max_length=20)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_client = True
        if commit:
            user.save()
            ClientProfile.objects.create(
                user=user,
                contact=self.cleaned_data['contact']
            )
        return user



