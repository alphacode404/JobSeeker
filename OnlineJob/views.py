from email.headerregistry import Group
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Applicant, Job, Note, Profile

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
    passed = Job.objects.all().count


    context = {
        
    }
    return render(request, 'pages/dashboard.html', context)


@unathenticated_user
def register(request):

    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            # group = Group.objects.get(name='applicant')
            # user.group.add(group)

            # Profile.objects.create(user=user, 
            # name=user.username, )

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
    return render(request, 'pages/company-index.html')


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




@login_required(login_url='login')
def applied(request):
    return render(request, 'pages/applied.html')



def logoutuser(request):
    logout(request)
    return redirect('login')



def note(request):
    notes = Note.objects.filter(user=request.user).order_by('-date')

    context = {
        'notes': notes
    }
    
    return render(request, 'pages/note.html', context)

def noteupdate(request):

    if request.method == "POST":
        company = request.POST['company']
        position = request.POST['position']
        date = request.POST['date']
        text = request.POST['text']
        document = request.FILES['document']

        new_note = Note(company=company, position=position, date=date, text=text, document=document)
        new_note.user = request.user
        new_note.save()

        messages.success(request, "Note was successfully added")
        print(new_note)
        return redirect('note')

    
    return render(request, 'pages/note.html')



def notedelete(request, pk):

    note = Note.objects.get(id=pk)
    if request.method == "POST":
        note.delete()
        return redirect('note')

    context = {
        'note':note
    }

    return render(request, 'pages/deletenote.html', context)


