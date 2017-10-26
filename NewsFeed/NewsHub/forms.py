from django import forms
from django.contrib.auth.forms import UserCreationForm
from NewsHub.models import WorldData, CountryData, RoleData, UserClass, \
    get_worlds_list, get_country_list, get_roles_list


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254,
                             required=True,
                             label='Username',
                             help_text='Enter your email address', )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['world'] = forms.ChoiceField(choices=get_worlds_list())
        self.fields['country'] = forms.ChoiceField(choices=get_country_list())
        self.fields['role'] = forms.ChoiceField(choices=get_roles_list())

    class Meta:
        model = UserClass
        fields = ('email', 'password1', 'password2', 'world', 'country',
                  'role')


class LogInForm(UserCreationForm):
    # email = forms.CharField(max_length=254,
    #                         required=True,
    #                         label='Username',
    #                         help_text='Enter your email address', )

    class Meta:
        model = UserClass
        fields = ('username', 'password')
