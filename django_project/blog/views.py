from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post #. means its in the package
from django.views.generic import (
  ListView,
  DetailView,
  CreateView,
  UpdateView,
  DeleteView
)
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin #! can't use decorator to set a class view to logged in only, so this mixin is used and passed to the class argument
from django.contrib.auth.models import User
# Create your views here.



def home(request):
  #gets list of dicts, pass to render()
  #allow us to access data in the dicts in the templates
  context = {
    'posts':Post.objects.all()#! ignore if linter complains
  }

  return render(request,'blog/home.html',context)#string is the file path inside the template folder

class PostListView(ListView):#! class based view
  model = Post
  template_name = 'blog/home.html' #! <app>/<model>_<viewtype>.html is the django template naming convention
  context_object_name = 'posts'
  ordering = ['-date_posted'] #! show newest post first
  paginate_by = 5#! pagination, 2 post per page

class UserPostListView(ListView):#! copy from previous class, display posts of a certain user
  model = Post
  template_name = 'blog/user_posts.html'#! <app>/<model>_<viewtype>.html is the django template naming convention
  context_object_name = 'posts'
  paginate_by = 5#! pagination, 2 post per page

  def get_queryset(self):
    user = get_object_or_404(User,username = self.kwargs.get('username'))
    return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):#! class based view
  model = Post

class PostCreateView(LoginRequiredMixin,CreateView):#! class based view
  model = Post
  fields = ['title','content']

  def form_valid(self,form):
    form.instance.author = self.request.user
    messages.success(self.request,f'Posted made!')
    return super().form_valid(form)
  
  

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):#! class based view
  model = Post
  fields = ['title','content']

  def form_valid(self,form):
    form.instance.author = self.request.user
    messages.success(self.request,f'Posted modified!')
    return super().form_valid(form)
  def test_func(self):#! use UserPassesTestMixin to only allow the original author to edit the post
    post = self.get_object()
    if self.request.user == post.author:
      return True
    return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):#! class based view
  model = Post
  success_url ='/'#! if deleted, redirect to home page

  def test_func(self):#! use UserPassesTestMixin to only allow the original author to edit the post
    post = self.get_object()
    if self.request.user == post.author:
      return True
    return False
  
  


def about(request):
  return render(request,'blog/about.html',{'title':'About'})
