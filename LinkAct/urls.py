"""TermProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.start_page_show, name='start_page_url'),
	url(r'linker/', views.linker_page_show, name='linker_page_url'),
    url(r'activities/', views.activities_page_show, name='activities_page_url'),
    url(r'explore/', views.explore_page_show, name='explore_page_url'),
    url(r'share/', views.share_page_show, name='share_page_url'),
    
]