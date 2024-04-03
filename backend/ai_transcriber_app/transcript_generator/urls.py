from django.urls import path
from . import views
urlpatterns = [
   path('', views.index, name='index'),
   path('login', views.user_login, name='login'),
   path('signup',views.user_signup, name='signup'),
   path('logout',views.user_logout, name='logout'),
   path('allscripts',views.all_scripts, name='all-scripts'),

]