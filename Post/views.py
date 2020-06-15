from django.shortcuts import render, get_object_or_404, redirect
# from django.shortcuts import

# Create your views here.
from .models import Post
from .forms import PostForm
from django.contrib import messages


def all_posts(request):
    all_posts = Post.objects.filter(active=True)
    context = {
        'all_posts': all_posts,
    }
    return render(request, 'all_posts.html', context)


def post(request, id):
    # post = Post.objects.get(id=id)
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post,
    }
    return render(request, 'detail.html', context)


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, 'Post created successfully')
            return redirect('/')

    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def edit_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES or None, instance=post)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('/')

    else:
        form = PostForm(instance=post)
    context = {
        'form': form,
    }
    return render(request, 'edit.html', context)
