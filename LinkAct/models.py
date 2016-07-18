from django.db import models
from datetime import date

class Front(models.Model):
	a = ''
	
class User(models.Model):
	#用户名
	username = models.CharField(max_length = 20)
	#密码
	password = models.CharField(max_length = 20)
	#ID
	id = models.CharField(max_length = 50)
	#生日
	birthday = models.DateField(default = date.today)
	#好友
	friends = list()
	#主页地址
	website = models.URLField()
	#邮箱
	email = models.EmailField()
	#所在城市
	city = models.CharField(max_length = 20)
	#头像
	head = models.ImageField(upload_to = 'image/')
	#已完成活动：参与&发起
	participate_terminative_acts = list()
	create_ongoing_acts = list()
	#进行中活动：参与&发起
	participate_terminative_acts = list()
	create_ongoing_acts = list()
	#评论过的活动
	commented_acts = list()
	#性别
	gender = models.CharField(max_length = 20)
	#兴趣
	interests = list()

	def __str__(self):
		return self.username
		
class activity(models.Model):
	#状态
	status = models.CharField(max_length = 20)
	#发起人ID
	creator = models.CharField(max_length = 20)
	#参与人ID
	participants = list()
	#地点
	locale = models.CharField(max_length = 20)
	#主题
	theme = models.CharField(max_length = 20)
	#发起时间
	create_date = models.DateField(default = date.today)
	#开始时间
	start_date = models.DateField(default = date.today)
	#结束时间
	end_data = models.DateField(default = date.today)
	#发起介绍
	introduction = models.TextField()
	#点赞人
	supporters = list()

class interest(models.Model):
	id = models.CharField(max_length = 50)
	content = models.CharField(max_length = 20)

