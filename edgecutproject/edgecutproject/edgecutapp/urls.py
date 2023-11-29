from .import views
from django.urls import path
app_name = 'edgecutapp'
urlpatterns = [
    path('', views.fun , name='fun'),
    path('about.html/',views.about,name='about'),
    path('furniture.html/',views.furniture,name='furniture'),
    path('blog.html/',views.blog,name='blog'),
    path('contact.html/',views.contact,name='contact'),
    path('register/',views.login,name='login'),
    path('loginform/',views.loginform,name='loginform'),
    path('logout/',views.logout,name="logout"),

]