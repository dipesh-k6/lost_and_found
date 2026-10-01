from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm #can also use AuthenticationForm for Login
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm

def register_user(request):
    """_summary_
            user registration form
    _extended_summary_
            handles user registration/data_validation and redirect to login page
    """    

    if request.method == 'POST':
       form =  UserCreationForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('login_page')
    else:
        form = UserCreationForm()

    return render(request, 'authentication/register.html', {"form":form})

def login_user(request):
    """_summary_
            user login form
    _extended_summary_
            handles user login and start session
    """    

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, 
                                username = data["username"],
                                password = data["password"])

            if user is not None:
                login(request, user)
                return redirect("dashboard_page")
            else:
                form.add_error(None, "Invalid username or password")

    else:
        form = LoginForm()

    return render(request, 'authentication/login.html', {"form":form})

def logout_user(request):
    """
    _summary_
        logout function

    _extended_summary_
        logs user out and redirect to dashboard page
    """    
    if request.method == "POST":
        logout(request)

    return redirect("dashboard_page")
    