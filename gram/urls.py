from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url('^search/', views.search_users, name='search_users'),
    url('^home/', views.home, name='home'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^new/post$', views.post_new, name='new_post'),
    
]
