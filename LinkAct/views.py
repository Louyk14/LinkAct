from django.shortcuts import render
from .models import Post
# Create your views here.
def start_page_show(request):
	start_page = Post.objects.all() 
	return render(request, 'LinkAct/start_page.html',
		{'stc':stc})
# Create your views here.
