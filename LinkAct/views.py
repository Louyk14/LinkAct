from django.shortcuts import render
from .models import Post
# Create your views here.
def start_page_show(request):
	start_page = Post.objects.all() 
	return render(request, 'LinkAct/start_page.html',
		{'stc':stc})
		
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

#创建活动
def to_create_act():
    
    return render(request, '创建活动网页', {'创建网页的用户信息——本人信息'})

#创建完成
def over_create_act():
    return render(request, '跳转至某网页', {'无参数'})

#参加活动
def enter_act():
    return render(request, '可跳转可不跳', {'无参数'})

#退出活动
def exit_act():
    return render(requset, '同上', {'无参数'})

#查看活动信息
def check_act_msg():
    #按下按钮后根据按钮活动id获取活动信息
    return render(request, '统一前缀 + 活动id', {'获取的或活动信息'})

#登录
def log_in():
    #根据用户名找到对应用户信息及信息网页
    return render(request, '用户信息网页或主页', {'用户信息'})

#登出
def log_out():
    return render(request, '', {'无参数'})

#查看个人信息
def check_personal_msg():
    return render(request, '个人信息页面', {'同logIn'})

#评价活动 —— 此处应有评价结构体
def evaluate_act():
    return render(request, '评价页面', {})

#完成评价
def finish_evaluate():
    return render(request, '跳转至主页或其它', {'用户信息及活动信息'})

#查找活动   //搜索页面不同于主页面
def search_act():
    return render(request, '搜索页面结果/search/?q=搜索内容', {})

#返回主页面按钮
def return_mainpage():
    return render(request, '主页面url', {'无参数'})

#添加好友
def request_for_friend():
    return render(request, '??弹窗或新页面', {})

#分享活动   按下分享按钮，页面可跳转可不跳转
def share_act():
    return reder(request, '弹窗？不跳转网页？', {})


# Create your views here.
