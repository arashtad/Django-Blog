from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import redirect

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts':posts})

def addNewPost(request):
    if request.method == "POST":
        form = BlogForm(request.POST, files = request.FILES)
        if form.is_valid:
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = BlogForm()
    return render(request,'new_post_form.html', {'form':form})

  
def post_details(request, slug):
    post = Post.objects.get(slug=slug)
    comments = Comment.objects.order_by("-created_date")
    new_comment = None
    if request.method == "POST":
        form = CommentForm(request.POST or None)
        if form.is_valid():
            new_comment = form.save(commit = False)
            new_comment.post = post
            new_comment.save()
            return render(request, "add_comment.html")
    else:
        form = CommentForm()
    return render(request, "add_comment.html", {'form': form, 'post':post , 'comments':comments, 'new_comment':new_comment })

def delete_post(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == "POST":
        post.delete()
        return redirect("home")
    return render(request, 'delete.html', {'post': post})

