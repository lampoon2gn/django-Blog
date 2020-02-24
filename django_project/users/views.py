from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
  if request.method == 'POST':#! if a POST request, fill the form with data in request
    form = UserCreationForm(request.POST)
    if form.is_valid():#* check done by django
      form.save#* if check is passed, save user
      username = form.cleaned_data.get('username') #! username is in cleaned_data dictionary
      messages.success(request,f'Account created for {username}!')
      return redirect('blog-home')
    else:
      messages.warning(request,f"Something's not right...Please check your form!")
  else:#! not POST request, display empty form
    form = UserCreationForm()
  return render(request,'users/register.html',{'form':form})

  # message.debug
  # message.info
  # message.success
  # message.warning
  # message.error