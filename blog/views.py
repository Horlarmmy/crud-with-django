from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from .models import Post, Comment
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CommentForm
from django.forms import ModelForm, widgets

class PostShow(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
   model = Post
   template_name = 'post_details.html'
 
class PostNew(generic.CreateView):
	model = Post
	template_name = 'post_new.html'
	fields = ['title', 'author', 'content']
class PostDelete(generic.DeleteView):
	model = Post
	template_name ='post_delete.html'
	success_url = reverse_lazy('index')
	
class PostUpdate(generic.UpdateView):
	model = Post
	template_name ='post_edit.html'
	fields =['title', 'content']
	
class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment.html'
    widgets = {
            'post': widgets.HiddenInput
        }
    success_url = reverse_lazy('index')
     
     
def signup(request):

    if request.user.is_authenticated:
        return redirect('account/login/')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username,password = password)
            login(request, user)
            return redirect('/account/login')
            print('Login to complete your registration')
        
        else:
            return render(request,'signup.html',{'form':form})
    
    else:
        form = UserCreationForm()
        return render(request,'signup.html',{'form':form})
        
def signout(request):
    logout(request)
    return redirect('/account/login')
    print('You have successfully logged out!')
        
def Dashboard(request):
	return render(request, 'dashboard.html')