from django.shortcuts import render
from django.http import HttpResponse
from .models import Post #. means its in the package

# Create your views here.

posts=[
  {
    'author':'cole',
    'title':'this is title',
    'content':'this is content',
    'date_posted':'01/23/2020'
  },
  {
    'author':'jin',
    'title':'this is also title',
    'content':'this is also content',
    'date_posted':'04/05/2020'
  },
]

def home(request):
  #gets list of dicts, pass to render()
  #allow us to access data in the dicts in the templates
  context = {
    'posts':Post.objects.all()
  }

  return render(request,'blog/home.html',context)#string is the file path inside the template folder

def about(request):
  return render(request,'blog/about.html',{'title':'About'})