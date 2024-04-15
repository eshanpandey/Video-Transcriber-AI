from django.urls import path
from . import views
urlpatterns = [
   path('', views.index, name='index'),
   path('login', views.user_login, name='login'),
   path('signup',views.user_signup, name='signup'),
   path('logout',views.user_logout, name='logout'),
   path('allscripts',views.all_scripts, name='all-scripts'),
   path('generate-transcript',views.generate_transcript,name='generate-transcript'),
   path('full-article/<int:pk>/',views.full_article,name='full-article'),




]