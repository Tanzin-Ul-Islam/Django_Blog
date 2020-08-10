from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from login_app.forms import signupform, updateprofile_form, profilepic
# Create your views here.
def sign_up(request):
    diction={}
    registered=False
    form=signupform()
    if request.method=='POST':
        form=signupform(data=request.POST)
        if form.is_valid():
            form.save()
            registered=True
    diction.update({'form':form})
    diction.update({'registered': registered})
    return render(request, 'login_app/signup.html', context=diction)


def user_login(request):
    diction={}
    form=AuthenticationForm()
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    diction.update({'form':form})
    return render(request, 'login_app/login.html', context=diction)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def profile(request):
    return render(request,'login_app/profile.html',context={})

@login_required
def updateprofile(request):
    updated=False
    diction={}
    current_user=request.user
    form=updateprofile_form(instance=current_user)
    if request.method=='POST':
        form=updateprofile_form(request.POST,instance=current_user)
        if form.is_valid():
            form.save()
            updated=True
    diction.update({'form':form, 'updated':updated})
    return render(request, 'login_app/changeprofile.html', context=diction)
@login_required
def updatepass(request):
    diction = {}
    current_user = request.user
    form = PasswordChangeForm(current_user)
    if request.method=='POST':
        form=PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login_app:login'))
    diction.update({'form':form})
    return render(request, 'login_app/changePass.html', context=diction)

@login_required
def uploadprofilepic(request):
    diction={}
    form=profilepic()
    if request.method=='POST':
        form=profilepic(request.POST, request.FILES)
        if form.is_valid():
            user_obj=form.save(commit=False)
            user_obj.user=request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('login_app:profile'))
    diction.update({'form':form})
    return render(request, 'login_app/uploadpic.html', context=diction)
@login_required
def changeprofilepic(request):
    diction={}
    form=profilepic(instance=request.user.userprofile)
    if request.method=='POST':
        form=profilepic(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login_app:profile'))
    diction.update({'form': form})
    return render(request, 'login_app/uploadpic.html', context=diction)





