from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.views.generic import DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        return redirect('login')
    return render(request, 'signup.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)  # Provide the request and the authenticated user
            return redirect('home')  # Redirect the user to the home page
        else:
            return redirect('signup')

    return render(request, 'login.html')


def home(request):
    post=Blogpost.objects.all()
    context={'post':post}
    return render(request, 'home.html',context)

@login_required
def hi(request):
    return render(request,'home.html')

@login_required
def new_blog(request):
    if request.method == 'POST':
        form = BlogpostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogpostForm()
    return render(request, 'new_blog.html', {'form': form})

class BlogDetail(DetailView):
    model = Blogpost
    template_name = 'blogdetail.html'
    context_object_name = 'blog'


class BlogUpdate(UpdateView):
    model= Blogpost
    fields = ['title','content']
    template_name= 'new_blog.html'
    success_url= reverse_lazy('home')


class BlogDelete(DeleteView):
    model= Blogpost
    template_name= 'blogdelete.html'
    context_object_name='delete'
    success_url= reverse_lazy('home')


   

