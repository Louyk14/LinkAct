from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.start_page_class, name='start_page'),
]