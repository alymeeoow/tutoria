from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import SignupForm

from tutoria_app.models import UserProfile



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





def signin(request):
    if request.method == "POST":
        username_or_email = request.POST.get('email')  
        password = request.POST.get('password')

      
        if '@' in username_or_email:
            try:
                user = UserProfile.objects.get(email=username_or_email)
                username_or_email = user.username 
            except UserProfile.DoesNotExist:
                user = None
        else:
            user = None

      
        user = authenticate(request, username=username_or_email, password=password)

        if user is not None:
            login(request, user)
            return redirect('tutoria')  
        else:
            return render(request, 'users/login.html', {
                'error': True,
                'error_title': "Login Failed!",
                'error_message': "Invalid email/username or password. Please try again."
            })

    return render(request, 'users/login.html')



def logout_function(request):
    logout(request)
    return redirect('signin')  

def forgot (request):

    return render (request,'users/forgot.html')


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

















