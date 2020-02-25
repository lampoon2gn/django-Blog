from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm #! form we created in forms.py, includes an email filed
from django.contrib.auth.decorators import login_required #! decorator to declare view as logged in users only

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
  return render(request, 'users/profile.html')

  # message.debug
  # message.info
  # message.success
  # message.warning
  # message.error