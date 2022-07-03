from email.headerregistry import Group
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Applicant, Job, Profile

from .forms import ProfileForm, RegisterForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unathenticated_user, allowed_users


def index(request):

    jobs = Job.objects.all()

    context = {
        'jobs':jobs
    }

    return render(request, 'pages/index.html', context)



def about(request):
    return render(request, 'pages/about.html')


@login_required(login_url='login')
# @allowed_users(allowed_roles=[])
def dashboard(request):
    return render(request, 'pages/dashboard.html')


@unathenticated_user
def register(request):

    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account creation for {username} was successful')
            return redirect('login')

    context = {
        'form': form
    }
    print(form)

    return render(request, 'pages/register.html', context)



# @unathenticated_user
def loginuser(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('dashboard')
        else:
            messages.info(request," Invalid Credentials")
            return redirect('login')

    return render(request, 'pages/login.html')




@login_required(login_url='login')
def company(request):
    return render(request, 'pages/company.html')


@login_required(login_url='login')
def profile(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            messages.success(request, "Profile updated Successfully")
            return redirect('profile')

            # print('form')

    context = {'form': form }
    return render(request, 'pages/user-profile.html', context)


@login_required(login_url='login')
def cv(request):
    return render(request, 'pages/cv.html')

@login_required(login_url='login')
def jobdetial(request):
    return render(request, 'pages/jobdetail.html')


@login_required(login_url='login')
def note(request):
    return render(request, 'pages/note.html')


def logoutuser(request):
    logout(request)
    return redirect('login')





