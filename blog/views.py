from urllib.parse import quote_plus

from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from blog.models import post
from blog.forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.db.models import Q

# Create your views here.

def post_list(request):
    posts_list = post.objects.all()
    query = request.GET.get("q")
    if query:
        posts_list = posts_list.filter(
            Q(title__icontains=query)|
            Q(post_content__icontains=query)
        ).distinct()
        print(posts_list)
    paginator = Paginator(posts_list, 10)  # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not integer deliver first page
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context_data={
        'posts_list': posts
    }
    return render(request, "blog/post_list.html", context_data)


def post_create(request):

    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    if not request.user.is_authenticated():
        raise Http404

    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        instance.user = request.user
        messages.success(request, "Successfully created")
        return redirect('blog:post_list')

    context ={
        'form': form
    }
    return render(request, "blog/post_create.html", context)


def post_detail(request, slug):

    instance = get_object_or_404(post, slug =slug)
    share_string = quote_plus(instance.post_content)
    context_data = {
        "title" : instance.title,
        "post" : instance,
        "share_string" : share_string
    }
    return render(request, "blog/post_detail.html", context_data)


def post_update(request, slug):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(post, slug=slug)
    # Remember putting or None
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Updated")
        return redirect('blog:post_detail', slug=instance.slug)

    context = {
        'form' : form,
        'instance' : instance
    }

    return render(request, "blog/post_update.html", context)


def post_delete(request, slug):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(post,  slug=slug)
    instance.delete()
    return redirect('blog:post_list')
