from django.db import models

# Create your models here.
#show what front page need
class Front(models.Model):
	a = 'aaaa'
	
from django import forms
from .models import MyUser
from .models import activity
from .models import interest

#注册信息
class RegisterForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('uername', '')

#创建活动信息
class ActForm(forms.ModelForm):
    class Meta:
        model = activity
        fields = ('locale', 'theme', 'start_date', 'end_data', 'introduction')

#发起评论信息
class CommentForm(form.ModelForm):
    class Meta:
        model = interest
        fields = ('content', 'id')
