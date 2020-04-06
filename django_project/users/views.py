from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm #! form we created in forms.py, includes an email filed
from django.contrib.auth.decorators import login_required #! decorator to declare view as logged in users only

#from django.contrib.auth.models import User#! attempt to get user email

# Create your views here.
def register(request):
  if request.method == 'POST':#! if a POST request, fill the form with data in request
    form = UserRegisterForm(request.POST)
    if form.is_valid():#* check done by django
      form.save()#* if check is passed, save user
      username = form.cleaned_data.get('username') #! username is in cleaned_data dictionary
      messages.success(request,f'Account created for {username}!')
      return redirect('login')
    else:
      messages.warning(request,f"Something's not right...Please check your form!")
  else:#! not POST request, display empty form
    form = UserRegisterForm()
  return render(request,'users/register.html',{'form':form})

@login_required #! decorator to declare view as logged in users only
def profile(request):
  if request.method == 'POST':
    u_form = UserUpdateForm(request.POST, instance=request.user)#! fill in the data of the current user
    p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)#! if user is updating, pass the new data and image FILE user uploaded
    if u_form.is_valid() and p_form.is_valid():
      u_form.save()
      p_form.save()
      messages.success(request,f'Profile updated!')
      return redirect('profile')

  else:
    u_form = UserUpdateForm(instance=request.user)#! fill in the data of the current user
    p_form = ProfileUpdateForm(instance=request.user.profile)

  context = {
    'u_form':u_form,
    'p_form':p_form
  }
  return render(request, 'users/profile.html',context)

  # message.debug
  # message.info
  # message.success
  # message.warning
  # message.error

# #!attempt to force log in before visiting password reset
# @login_required #! decorator to declare view as logged in users only
# def password_reset(request):
#   if request.method == 'POST'
#   entered_email = 
#   logged_email = user.email
