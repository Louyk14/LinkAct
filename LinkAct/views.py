from django.shortcuts import render
from .models import MyUser
from .models import Activity
from django.shortcuts import render
from django.contrib import auth
from django.core.mail import send_mail
		
#
#如下的表单内容： 
#<form action="/save" method="post"> 
#       <input type="hidden" name="file_name" value={{file_name}}> 
#       <input name="submit" type="submit" value="save" size="" />      
#       <input name="submit" type="submit" value="cancel" size="" /> 
#</form> 
#我在服务器端可以通过request.post.get('submit') 为save 或者 cancel来判断用户点击了哪个变量，

#方法2
#form action="" method="post">
#……
#<input type="submit" name="install" value="安装">
#……
#<input type="submit" name="server" value="执行">
#</form>
#只要在按钮上添加name值，兄弟连如上面红色部分，然后在后台进行判断，即view.py，如下代码：
#def install(request):
#    '''服务安装'''
#    iplist = IP.objects.all()
#    server_list = AddServer.objects.all()
#	mserver_list = MServer.objects.all()
#    if request.method == "POST":
#        if request.POST.has_key('install'):    #这里判断，如果是name值为install的，则执行此段代码
#           ……代码段省略……
#        else:   #这里判断，如果不是name值为install的，则执行此段代码，因为我们就只有2个name，所以就不用elif request.POST.has_key('server'):了

# Create your views here.
#导航栏
def start_page_show(request):
	return render(request, 'LinkAct/start_page.html',
		{})

def linker_page_show(request):
	return render(request, 'LinkAct/linker_page.html', 
		{})

def explore_page_show(request):
	return render(request, 'LinkAct/explore_page.html', 
		{})

def share_page_show(request):
	return render(request, 'LinkAct/share_page.html', 
		{})

def activities_page_show(request):
	return render(request, 'LinkAct/activities_page.html', 
		{})

#用户注册
def user_register(request):
	params = request.POST
	registerForm = RegisterForm(params)
	#一系列合法性判定

	#判定完毕
	user = User()
	user.username = registerForm.username
	user.password = registerForm.password
	user.email = registerForm.email
	user.MyUser.nickname = registerForm.nickname
	user.MyUser.birthday = registerForm.birthday
	user.MyUser.website = registerForm.website
	user.MyUser.city = registerForm.city
	user.MyUser.head = registerForm.head
	user.MyUser.gender = registerForm.gender
	user.MyUser.interests = registerForm.gender
	
	#myUser.user.save()
	user.save()

	return render(request, '', {})
		

#创建活动
def to_create_act():
	return render(request, '创建活动网页', {'创建网页的用户信息——本人信息'})

#创建完成
def over_create_act(request):
	#在全局绑定函数中判断按下了哪个按钮，此处需知道当前用户名，默认活动form为ActForm
	params = request.POST
	form = ActForm(params)
	if form.is_valid():
		newAct = form.save(commit=False)
		newAct.creator = request.user.username
		newAct.save()
		Activity.order_by("create_date")
		form = ActForm()
	show_acts = Activity.objects.all()
	if len(show_acts) >= 10:
		show_acts = show_acts[:10]   
	return render(request, '跳转至查看活动界面', {'show_acts': show_acts})

#参加活动，传入活动id，如何根据request获取当前用户id，此处还未判断是否人满
def enter_act(request, act_id):
	to_entered_act = Activity.objects.get(id = act_id)
	to_entered_act.participants.push(request.user.id)

		#向用户正参加活动列表中添加
	return render(request, '可跳转可不跳', {'无参数'})

#退出活动
def exit_act(request, act_id):
	to_entered_act = Activity.objects.get(id = act_id)
	to_entered_act.participants.remove(request.user.id)

	#从用户正参加列表中删除
	return render(requset, '同上', {'无参数'})

#查看活动信息
def check_act_msg(request, act_id):
	#按下按钮后根据按钮活动id获取活动信息
	to_check_act = Activity.objects.get(id = act_id)
	
	return render(request, '统一前缀 + 活动id', {'to_check_act': to_check_act})

#登录
def log_in(request):
	#根据用户名找到对应用户信息及信息网页
	log_username = request.POST['username']
	log_password = request.POST['password']
	user = auth.authenticate(username = log_username, password = log_password)
	if user is not None:
		if user.is_active:
			auth.login(request, user)
		else:
			#不匹配
			return
	return

	
#登出
#登出回到一切的首页
def log_out(request):
	auth.logout(request)
	#post without user
	return render(request, 'LinkAct/start_page.html', {})

#查看个人信息--可以通过使用request.user.MyUser.nickname获取附加信息
def check_personal_msg(request):
	return render(request, '个人信息页面', {'log_user': request.user})

#评价活动——需要评价Form，先定义为CommentForm
def evaluate_act(request, act_id):
	return render(request, '评价页面', {'act_id': act_id})

#完成评价
def finish_evaluate(request, act_id):
	params = request.POST
	form = CommentForm(params)
	if form.is_valid():
		newComment = form.save(commit=False)
		newComment.creator = request.user.username
		newComment.save()
		Activity.order_by("create_date")
		form = newComment()
	return render(request, '跳转至主页或其它', {'用户信息及活动信息'})

#查找活动   //搜索页面不同于主页面
def search_act(request):
	params = request.POST
	form = RequestForm(params)

	#不同检索方式
	if form.method == 'theme':
		show_answers = Activitys.filter(theme=form.content)
		return render(request, '搜索页面结果/search/?q=搜索内容', {'show_answers': show_answers})
	elif form.method == 'theme':
		show_answers = Activitys.filter(theme=form.content)
		return render(request, '搜索页面结果/search/?q=搜索内容', {'show_answers': show_answers})
	elif form.method == 'theme':
		show_answers = Activitys.filter(theme=form.content)
		return render(request, '搜索页面结果/search/?q=搜索内容', {'show_answers': show_answers})
	elif form.method == 'theme':
		show_answers = activitys.filter(theme=form.content)
		return render(request, '搜索页面结果/search/?q=搜索内容', {'show_answers': show_answers})

# #返回主页面按钮
# def return_mainpage():
# 	return render(request, '主页面url', {'无参数'})

#添加好友
def request_for_friend(request):
	return render(request, '??弹窗或新页面', {})

#分享活动   按下分享按钮，页面可跳转可不跳转
def share_act():
	#貌似要用到相关分享平台的API
	return render(request, '弹窗？不跳转网页？', {})

def send_emails():
	send_mail('wf', 'wf', "Louyk14@163.com", "Louyk14@163.com", fail_silently=False)



# Create your views here.
