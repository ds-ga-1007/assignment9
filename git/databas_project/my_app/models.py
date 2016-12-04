from django.db import models
#from django.contrib.auth.models import  AbstractBaseUser
from django import forms
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = AuthenticationForm(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = AuthenticationForm(username=username, password=password)
        return user

class RegistrationForm(forms.ModelForm):
    """
    Form for registering a new account.
    """
    username = forms.CharField(widget=forms.Widget.__name__, label="Username")
    password1 = forms.CharField(widget=forms.Widget.PasswordInput,
                                label="Password")
    password2 = forms.CharField(widget=forms.Widget.PasswordInput,
                                label="Password (again)")

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def clean(self):
        """
        Verifies that the values entered into the password fields match

        NOTE: Errors here will appear in ``non_field_errors()`` because it applies to more than one field.
        """
        cleaned_data = super(RegistrationForm, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        return self.cleaned_data

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class AuthenticationForm(forms.Form):
    """
    Login form
    """
    username = forms.CharField(widget=forms.widgets.TextInput)
    password = forms.CharField(widget=forms.widgets.PasswordInput)

    class Meta:
        fields = ['username', 'password']


class Cuisines(models.Model):
    name = models.CharField(max_length=20)
    TAG_TITLE = (
        (0, 'Italian'),
        (1, 'Chinese'),
        (3, 'Japanese'),
        (4, 'American'),
        (5, 'Vegan'),
        (6, 'Turkish'),
        (7, 'Soup'),
        (8, 'Spicy'),
        (9, 'Sweets'),
        (10, 'Diery-Free'),
        (11, 'Low-calorie'),
        (12, 'Main-dish'),
        (13, 'cake'),
    )

    variety = models.IntegerField(choices=TAG_TITLE)
    def __str__(self):
        return self.name

class Recipies(models.Model):
    rc_title = models.CharField(max_length=20)
    rc_howToMake = models.TextField()
    rc_serving =models.CharField(max_length=10)
    cuisines = models.OneToOneField(Cuisines)

    picture = models.ImageField(upload_to='profile_images/', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return self.user.username

class Review(models.Model):
    RATING_CHOICES = (
        (1, 'Awful!'),
        (2, 'No thanks!'),
        (3, 'Fine, I guess'),
        (4, 'Tasty delight!'),
        (5, 'Ambrosia of the gods!'),
    )
    recipies = models.ForeignKey(Recipies, null=True, blank=True)
    pub_date = models.DateTimeField('date published', null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    comment = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
    favorite = models.BooleanField(default=False)

class CookGroup_names(models.Model):
    groupname=models.CharField(max_length=100)
    def __str__(self):
        return self.groupname

class CookGroup(models.Model):
    #groupname = models.CharField(max_length=100)
    groupname=models.ForeignKey(CookGroup_names, null=True, blank=True)
    username=models.ManyToManyField(User)
    join_dt=models.BooleanField(default=True)

