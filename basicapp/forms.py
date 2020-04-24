#create forms heref
#forms for input
"""from django import forms
from django.contrib.auth.models import User
from basicapp.models import user_profile

class newform(forms.ModelForm):
    class Meta:
        model = user_profile
        fields = '__all__'
    def clean(self):
        data = self.cleaned_data
        return data

""" """class user_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['password',]"""

from django import forms
from django.contrib.auth.models import User
from basicapp.models import profile

class user_form(forms.Form):
    username = forms.CharField(max_length =12)
    password = forms.CharField(min_length=8,widget= forms.PasswordInput())
    first_name = forms.CharField()
    last_name = forms.CharField()
    birthdate = forms.DateField(widget=forms.SelectDateWidget(years=range(1980,2015)))
    site = forms.URLField()
    #picture = forms.ImageField()
class newpost(forms.Form):
    post_1 = forms.CharField()
class comment(forms.Form):
    comment_add = forms.CharField(max_length=24)
