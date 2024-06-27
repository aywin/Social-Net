from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import User, Electif

class ProfileForm(UserChangeForm):
    profile_pic = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'config-form-input'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'config-form-textarea'}), required=False)
    cover = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'config-form-input'}))
    nationality = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'config-form-input'}))
    promotion = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'config-form-input'}))
    graduation_date = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'config-form-input'}), required=False)
    phone_number = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'config-form-input'}))
    major = forms.ChoiceField(choices=User._meta.get_field('major').choices, required=False, widget=forms.Select(attrs={'class': 'config-form-select'}))
    option = forms.ChoiceField(choices=User._meta.get_field('option').choices, required=False, widget=forms.Select(attrs={'class': 'config-form-select'}))
    filiere = forms.ChoiceField(choices=User._meta.get_field('filiere').choices, required=False, widget=forms.Select(attrs={'class': 'config-form-select'}))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'config-form-input'}))
    mentoring_1A = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'config-form-input'}))
    mentoring_2A = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'config-form-input'}))
    mentoring_3A = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'config-form-input'}))
    linkedin = forms.URLField(required=False, widget=forms.URLInput(attrs={'class': 'config-form-input'}))
    other_links = forms.URLField(required=False, widget=forms.URLInput(attrs={'class': 'config-form-input'}))
    
    competence_concevoir_rechercher = forms.ChoiceField(choices=Electif.CONCEVOIR_RECHERCHER_MODULES, required=False, widget=forms.Select(attrs={'class': 'config-form-select'}))
    competence_developper_innover = forms.ChoiceField(choices=Electif.DEVELOPPER_INNOVER_MODULES, required=False, widget=forms.Select(attrs={'class': 'config-form-select'}))
    competence_produire_promouvoir_vendre = forms.ChoiceField(choices=Electif.PRODUIRE_PROMOUVOIR_VENDRE_MODULES, required=False, widget=forms.Select(attrs={'class': 'config-form-select'}))

    class Meta:
        model = User
        fields = [
            'profile_pic', 'bio', 'cover', 'nationality', 'promotion', 'graduation_date', 'phone_number',
            'major', 'option', 'filiere', 'email', 'mentoring_1A', 'mentoring_2A', 'mentoring_3A',
            'linkedin', 'other_links', 'competence_concevoir_rechercher', 'competence_developper_innover',
            'competence_produire_promouvoir_vendre'
        ]

from django import forms
from django.contrib.auth.models import User

class EditUserForm(forms.ModelForm):
    USER_GROUP_CHOICES = [
        ('student', 'Student'),
        ('alumni', 'Alumni'),
        # Add other groups as needed
    ]
    
    user_group = forms.ChoiceField(choices=USER_GROUP_CHOICES, widget=forms.Select(attrs={'class': 'config-form-input'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'user_group', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'config-form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'config-form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'config-form-input'}),
            'email': forms.EmailInput(attrs={'class': 'config-form-input'}),
        }



from django import forms
from django.contrib.auth.models import User

class RegisterUserForm(forms.ModelForm):
    user_group = forms.ChoiceField(
        choices=[('Alumni', 'Alumni'), ('Eleve', 'Élève')],
        widget=forms.RadioSelect(attrs={'class': 'config-form-input'}),
        required=True
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'config-form-input'}), required=True)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'config-form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'config-form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'config-form-input'}),
            'email': forms.EmailInput(attrs={'class': 'config-form-input'}),
        }
