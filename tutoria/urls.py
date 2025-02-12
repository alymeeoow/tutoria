"""
URL configuration for tutoria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from tutoria_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name ="index"),
    path('signup', views.signup,name ="signup"),
     path('forgot', views.forgot,name ="forgot"),
    path('signin', views.signin,name ="signin"),
    path('logout', views.logout_function,name ="logout"),
    path('find_tutor', views.find_tutor,name ="find_tutor"),
    path('tutoria', views.tutoria,name ="tutoria"),
    path('user_chat', views.user_chat,name ="user_chat"),
    path('subjects', views.subjects,name ="subjects"),
    path('subjects_2', views.subjects_2,name ="subjects_2"),
    path('user_about', views.user_about,name ="user_about"),
    path('user_about_2', views.user_about_2,name ="user_about_2"),
    path('congrats', views.congrats,name ="congrats"),
    path('teacher_profile', views.teacher_profile,name ="teacher_profile"),
    path('teacher_profile_2', views.teacher_profile_2,name ="teacher_profile_2"),
    path('parent_profile', views.parent_profile ,name ="parent_profile"),
    path('student_profile', views.student_profile ,name ="student_profile"),
  path('profile', views.profile ,name ="profile"),
    
]
