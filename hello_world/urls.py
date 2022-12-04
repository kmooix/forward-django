from django.urls import path, re_path
from hello_world import views

app_name = 'hello_world'

urlpatterns = [
    re_path('^register/$', views.register, name='register'),
    re_path('^user_login/$', views.user_login, name='user_login'),
    re_path('^dashboard/$', views.dashboard, name='dashboard'),
]
