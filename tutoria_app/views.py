from django.shortcuts import render,redirect
from django.contrib.auth import login
from .forms import SignupForm




def index (request):

    return render (request, "users/index.html")



def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'users/signup.html', {
                'form': SignupForm(),
                'success': True,
                'modal_title': "Signup Successful!",
                'modal_message': "Welcome to Tutoria! Your account has been created successfully."
            })
        else:
           
            if "password2" in form.errors:
                error_message = "Passwords do not match. Please try again."
            else:
                error_message = "Please fix the following errors:"
                for field, errors in form.errors.items():
                    error_message += f"\n{field.capitalize()}: {errors[0]}"

            return render(request, 'users/signup.html', {
                'form': form,
                'error': True,
                'error_title': "Signup Failed!",
                'error_message': error_message
            })

    else:
        form = SignupForm()

    return render(request, 'users/signup.html', {'form': form})




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


def profile(request):
  
    return render(request, 'users/profile.html')

















