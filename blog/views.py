from django.shortcuts import render,redirect
from blog.models import Post
from .models import Contact



# Create your views here.

def Home(request):

    #load data from Post Model
    posts = Post.objects.all()
    data ={
        'posts': posts
    }
    return render(request, 'index.html',data)

def About(request):
    return render(request,'about.html')

def ContactPage(request):
    return render(request, 'contact.html')

def post(request,url):
    post = Post.objects.get(url=url)
    data = {
        'post':post
    }
    return render(request,'post-details.html',data)

def contactData(request):
    if request.method == "POST":  # Use "POST" (uppercase)
        name = request.POST.get('name')  # Use request.POST (uppercase POST)
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        query = Contact(name=name, email=email, subject=subject, message=message)
        query.save()
        return redirect("/")
    return render(request, 'contact.html')
