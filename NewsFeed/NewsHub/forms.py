from django import forms
from django.contrib.auth.forms import UserCreationForm
from NewsHub.models import WorldData, CountryData, RoleData, UserClass


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254,
                             required=True,
                             label='Username',
                             help_text='Enter your email address', )

    world = forms.ModelChoiceField(
        queryset=WorldData.objects.all().values_list('world_name',
                                                     flat=True))

    country = forms.ModelChoiceField(
        queryset=CountryData.objects.all().values_list('country',
                                                       flat=True))

    role = forms.ModelChoiceField(
        queryset=RoleData.objects.all().values_list('role',
                                                    flat=True))

    class Meta:
        model = UserClass
        fields = ('email', 'password1', 'password2', 'world', 'country',
                  'role')


class LogInForm(UserCreationForm):
    email = forms.EmailField(max_length=254,
                             required=True,
                             label='Username',
                             help_text='Enter your email address', )

    class Meta:
        model = UserClass
        fields = ('email', 'password')
