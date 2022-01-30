from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Category,Post,PostComments
from django.views.generic.edit import CreateView,UpdateView
from .forms import PostCommentsforms,register
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def home(request):
    posts = Post.objects.all()
    cats = Category.objects.all()
    return render(request,'index.html',{'cats':cats,'posts':posts,'home':'active'})


def catogery(request):
    posts = Post.objects.all()
    cats = Category.objects.all()
    
    return render(request,'blog.html',{'cats':cats,'posts':posts,'catogery':'active'})



def postdetails(request,url):
    forms = PostCommentsforms(request.POST or None)
    if request.method == 'POST':
        forms = PostCommentsforms(request.POST)
        if forms.is_valid():
            forms.save()
            return HttpResponseRedirect('/')
        else:
            forms = PostCommentsforms()
            
    postcomments = PostComments.objects.all()
    posts = Post.objects.get(url=url)
    cats = Category.objects.all()
    all_posts = Post.objects.all()
    return render(request,'post-details.html',{'cats':cats,'posts':posts,'all_posts':all_posts,'forms': forms,'postcomments':postcomments})


    

class register(CreateView):
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    form_class = UserCreationForm
    # if request.method == 'POST':
    #     forms = register(request.POST)
    #     if forms.is_valid():
    #         forms.save()
    #         return HttpResponseRedirect('/')
        
    # else:
    #     forms = PostCommentsforms    
    
    # return render(request,'register.html',{'forms':forms})


# def login(request):
#     return render(request,'registration/login.html',{})

def all_post_related_to_catogery(request,url):
    catos = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=catos)
    return render(request,'all_post_related_to_one_catogery.html',{'catos':catos,'posts':posts})




