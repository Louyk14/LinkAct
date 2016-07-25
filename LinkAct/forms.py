from django import forms
from .models import MyUser
from .models import Activity
from .models import Interest
from datetime import date
from LinkAct import models

def get_interests_style():
    a = []

    for x in Interest.objects.all():
        t = (x.id, x.get_content())
        a.append(t)
        print(tuple(a))
    return tuple(a)


#注册信息
class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名',max_length = 20)
    password1 = forms.CharField(label='密码',widget=forms.PasswordInput())
    password2 = forms.CharField(label='再次确认密码',widget=forms.PasswordInput())
    nickname = forms.CharField(label='昵称',max_length = 20)
    email = forms.EmailField(label='电子邮箱')
    birthday = forms.DateField(label='生日',initial=date.today)
    city = forms.CharField(label='城市',max_length = 20)

    interest = forms.MultipleChoiceField(label = u'爱好', choices = get_interests_style(), widget = forms.CheckboxSelectMultiple())

class PersonalInfoForm(forms.Form):
    nickname = forms.CharField(label='昵称',max_length = 20)
    email = forms.EmailField(label='电子邮箱')
    birthday = forms.DateField(label='生日')
    city = forms.CharField(label='城市',max_length = 20)
    interest = forms.CharField(label='爱好',max_length = 50)

class SetPasswordForm(forms.Form):
    origin_password = forms.CharField(label='原始密码',widget=forms.PasswordInput())
    new_password1 = forms.CharField(label='新密码',widget=forms.PasswordInput())
    new_password2 = forms.CharField(label='再次确认新密码',widget=forms.PasswordInput())

#创建活动信息
class ActForm(forms.Form):
    locale = forms.CharField(max_length = 20)
    #主题
    theme = forms.MultipleChoiceField(label=u'活动类型', choices=get_interests_style(), widget=forms.CheckboxSelectMultiple())
    #开始时间
    start_date = forms.DateField(initial = date.today)
    #结束时间
    end_data = forms.DateField(initial = date.today)
    #发起介绍
    introduction = forms.CharField(max_length = 300)
        
#发起评论信息
class CommentForm(forms.Form):
    commenter = forms.IntegerField()
    score = forms.IntegerField()
    content = forms.CharField(max_length = 20)

class LogForm(forms.Form):
    username = forms.CharField(label='用户名',initial='',max_length=20)
    password = forms.CharField(label='密码',initial='',widget=forms.PasswordInput())
