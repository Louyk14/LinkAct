from django import forms
from .models import MyUser
from .models import Activity
from .models import Interest
from .models import ListField

#注册信息
class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 20)
    password1 = forms.CharField(max_length = 20)
    password2 = forms.CharField(max_length = 20)
    email = forms.CharField(max_length = 20)
    nickname = forms.CharField(max_length = 20)
    birthday = forms.DateField(default = date.today)
    website = forms.URLField()
    city = forms.CharField(max_length = 20)

#创建活动信息
class ActForm(forms.Form):
    #状态
    status = forms.CharField(max_length = 20)
    #发起人ID
    creator = forms.IntegerField()
    #参与人ID
    participants = ListField(default = [])
    #地点
    locale = forms.CharField(max_length = 20)
    #主题
    theme = forms.CharField(max_length = 20)
    #发起时间
    create_date = forms.DateField(default = date.today)
    #开始时间
    start_date = forms.DateField(default = date.today)
    #结束时间
    end_data = forms.DateField(default = date.today)
    #发起介绍
    introduction = forms.TextField()
    #点赞人
    supporters = ListField(default = [])

        
#发起评论信息
class CommentForm(forms.Form):
    commenter = models.IntegerField()
    score = models.IntegerField()
    content = models.CharField(max_length = 20)

class LogForm(forms.Form):
    username = forms.CharField(max_length = 20)
    password = forms.CharField(max_length = 20)
