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
def toCreateAct():   
    return render(request, '创建活动网页', {'参数'})

#创建完成
def overCreateAct():
    return render(request, '跳转至某网页', {})

#参加活动
def enterAct():
    return render(request, '可跳转可不跳', {})

#退出活动
def exitAct():
    return render(requset, '同上', {})

#查看活动信息
def checkActMsg():
    return render(request, '统一前缀 + 活动id', {})

#登录
def logIn():
    return render(request, '', {})

#登出
def logOut():
    return render(request, '', {})

#查看个人信息
def checkPersonalMsg():
    return render(request, '个人信息页面', {})

#评价活动
def evaluateAct():
    return render(request, '评价页面', {})

#完成评价
def finishEvaluate():
    return render(request, '跳转至主页或其它', {})

#查找活动   //搜索页面不同于主页面
def searchAct():
    return render(request, '搜索页面结果/search/?q=搜索内容', {})

#返回主页面按钮
def returnMainPage():
    return render(request, '主页面url', {})

#添加好友
def requestForFriend():
    return render(request, '??弹窗或新页面', {})

#分享活动   按下分享按钮，页面可跳转可不跳转
def shareAct():
    return reder(request, '', {})


# Create your views here.
