from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from .forms import *
# Create your views here.

def details(request, category_slug,slug):
    post = get_object_or_404(Post, slug=slug,status="Published")
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('post_details',category_slug=category_slug, slug=slug)
    else:
        form = CommentForm()
    
    #comments = post.comments.all()  # Retrieve all comments for this post
    
    return render(request, 'blog/post.html', {'post': post, 'form': form, })

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status="Published")


    return render(request,"blog/category.html",{'category': category, 'posts': posts})

def search(request):
    query = request.GET.get('query','')

    post = Post.objects.filter(status="Published").filter(Q(title__icontains=query) | Q(intro__icontains=query)| Q(body__icontains=query) )

    return render(request, 'blog/search.html',{'post':post,'query':query})

def robots_txt(request):
    """prevent bots from accessing the admin"""
    text = [
        "User-Agent:*",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text),content_type='text/plain')