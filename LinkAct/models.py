from django.db import models

# Create your models here.
#show what front page need
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
	birthday = models.CommaSeparatedIntegerField(max_length = 3)
	#好友
	friends = models.JSONField(max_length = 300)
	#主页地址
	website = models.URLField()
	#邮箱
	email = models.EmailField()
	#所在城市
	city = models.CharField(max_length = 20)
	#头像
	head = models.ImageField(upload_to = 'image/')
	#已完成活动：参与&发起
	participate_terminative_acts = models.JSONField(max_length = 300)
	create_ongoing_acts = models.JSONField(max_length = 300)
	#进行中活动：参与&发起
	participate_terminative_acts = models.JSONField(max_length = 300)
	create_ongoing_acts = models.JSONField(max_length = 300)
	#评论过的活动
	commented_acts = models.JSONField(max_length = 300)
	#性别
	gender = models.CharField(max_length = 20)
	#兴趣
	interests = models.JSONField(max_length = 300)

	def __str__(self):
		return self.username
		
class activity(models.Model):
	#状态
	status = models.CharField(max_length = 20)
	#发起人ID
	creator = models.CharField(max_length = 20)
	#参与人ID
	participants = models.JSONField(max_length = 300)
	#地点
	locale = models.CharField(max_length = 20)
	#主题
	theme = models.CharField(max_length = 20)
	#发起时间
	create_date = models.DateField()
	#开始时间
	start_date = models.DateField()
	#结束时间
	end_data = models.DateField()
	#发起介绍
	introduction = models.TextField()
	#点赞人
	supporters = models.JSONField(max_length = 300)

class interest(models.Model):
	id = models.CharField(max_length = 50)
	content = models.CharField(max_length = 20)
