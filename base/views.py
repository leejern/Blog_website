from django.shortcuts import *
from blog.models import *
from .forms import *

# Create your views here.    prepopulated_fields = {'slug':('title',)}

def home(request):
    posts = Post.objects.filter(status="Published")
    local = {
        "posts": posts
    }
    return render(request,'base/index.html', local)

def about(request):
    return render(request,'base/about.html')

def contact(request): 
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact' , )
    else:
        form = ContactForm()
     
    #comments = post.comments.all()  # Retrieve all comments for this post
    
    
    return render(request,'base/contact.html',{'form':form})