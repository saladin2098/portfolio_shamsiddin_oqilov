from turtle import title
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import json
from django.db.models import Q

from .models import Post, PostCategory, Comment
# Create your views here.

def blog_view(request):
    posts = Post.objects.all()
    post_categories = PostCategory.objects.all()
    qs_json = json.dumps(list(Post.objects.values()), default=str)

    
    context = {
        'posts': posts,
        'post_categories': post_categories,
        'qs_json': qs_json,
    }
    return render(request, 'html/blog_topbar.html', context)


@login_required(login_url='login-page')
def inside_the_post(request, pk):
    post = Post.objects.get(id=pk)
    user = request.user

    if user not in post.viewers.all():
        post.viewers.add(user)
        post.save()
    context = {
        'post': post,
        'user': user,
    }
    return render(request, 'post/single.html', context)


@login_required(login_url='login-page')
def save_like(request, pk):
    user = request.user
    print(user)
    post = Post.objects.get(id=pk)
    if user in post.disliked_users.all():
        post.disliked_users.remove(user)
    post.liked_users.add(user)
    post.save()

    return redirect('inside-post', pk=pk)

@login_required(login_url='login-page')
def unlike(request, pk):

    post = Post.objects.get(id=pk)
    post.liked_users.remove(request.user)
    post.save()

    return redirect('inside-post', pk=pk)


@login_required(login_url='login-page')
def dislike(request, pk):
    user = request.user
    post = Post.objects.get(id=pk)
    if user in post.liked_users.all():
        post.liked_users.remove(user)
    post.disliked_users.add(user)
    post.save()

        
    return redirect('inside-post', pk=pk)
    

@login_required(login_url='login-page')
def undislike(request, pk):

    post = Post.objects.get(id=pk)
    post.disliked_users.remove(request.user)
    post.save()

    return redirect('inside-post', pk=pk)



def save_comment(request, post_id):
    post = Post.objects.get(id=post_id)
    user = request.user
    comment = Comment()
    if request.POST:
        text = request.POST.get('text')
        if text != '':
            comment.post = post
            comment.user = user
            comment.text = text
            comment.save()
    return redirect('inside-post', pk=post_id)


