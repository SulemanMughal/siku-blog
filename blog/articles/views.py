from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# ? Local Models
from .models import (
    Post
)

# ? Import Configurations
from django.conf import settings

# ? Home View
def index(request):
    template_name= "articles/index.html"
    object_list = Post.publish_objects.order_by('-created_at')
    paginator = Paginator(object_list, settings.PAGINATION_OBJECT_COUNTER)

    # ? 'page' parameter in GET request
    page = request.GET.get('page')

    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    context={
        "posts" : post_list,
        'page': page,
    }
    return render(request, template_name, context)

# ? Specific Blog Post Details View
def details(request, title):
    template_name= "articles/details.html"
    try:
        post = Post.publish_objects.get(slug = title)
    except Post.DoesNotExist:
        messages.error(request, "Requested blog does not exist.")
        return redirect(reverse("index"))
    context={
        "post" : post
    }
    return render(request, template_name, context)

# ? Search Blog Posts by Title
def search(request):
    template_name= "articles/search.html"
    
    query=request.GET.get("query")

    if query:
        object_list= Post.publish_objects.filter(title__icontains=query).order_by('-created_at')
        paginator = Paginator(object_list, settings.PAGINATION_OBJECT_COUNTER)

        # ? 'page' parameter in GET request
        page = request.GET.get('page')

        try:
            post_list = paginator.page(page)
        except PageNotAnInteger:
            post_list = paginator.page(1)
        except EmptyPage:
            post_list = paginator.page(paginator.num_pages)

        context={
            'posts': post_list,
            "query" : query,
            "search_results" : object_list.count()
        }
        return render(request, template_name, context)
    return redirect(reverse("index"))