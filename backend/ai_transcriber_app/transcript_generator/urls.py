from django.urls import path
from . import views
urlpatterns = [
   path('', views.index, name='index'),
   path('login', views.login, name='login'),
   path('signup',views.signup, name='signup'),
   path('allscripts',views.all_scripts, name='all-scripts'),

]