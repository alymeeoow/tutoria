from django.shortcuts import render,render

# Create your views here.




def index (request):

    return render (request, "users/index.html")


def signup (request):

    return render (request,'users/signup.html')


def signin (request):

    return render (request,'users/login.html')


def find_tutor (request):

    return render (request,'users/find_tutor.html')



def tutoria(request):
  
    return render(request, 'users/tutoria.html')



def user_chat(request):
  
    return render(request, 'users/chat.html')


def subjects(request):
  
    return render(request, 'users/subjects.html')


def subjects_2(request):
  
    return render(request, 'users/subjects_2.html')




def user_about(request):
  
    return render(request, 'users/user_about.html')



def user_about_2(request):
  
    return render(request, 'users/user_about_2.html')


def congrats(request):
  
    return render(request, 'users/congrats.html')


def teacher_profile(request):
  
    return render(request, 'users/teacher_profile.html')


def teacher_profile_2(request):
  
    return render(request, 'users/teacher_profile_2.html')



def parent_profile(request):
  
    return render(request, 'users/parent_profile.html')



def student_profile(request):
  
    return render(request, 'users/student_profile.html')
















