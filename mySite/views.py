from django.shortcuts import render, get_object_or_404
from .models import Category, Post
from django.utils.translation import gettext as _

def index(request):
    categories = Category.objects.all()
    recent_posts = Post.objects.order_by('-pub_date')[:5]
    return render(request, 'mySite/index.html', {'categories': categories, 'recent_posts': recent_posts})

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category)
    title = Category.objects.all()
    return render(request, 'mySite/category.html', {'category': category, 'posts': posts, 'date_format': 'd.m.Y в H:i'})

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    category = post.category  # Access the category attribute of the specific post
    return render(request, 'mySite/post.html', {'post': post, 'category': category, 'date_format': 'd.m.Y в H:i'})

def new_page(request, page_name):
    data = request.POST.get('data', None)

    if page_name and data is not None:
        page_name+=".html"
        return render(request, page_name, {'data': data})
    elif page_name:
        page_name+=".html"
        return render(request, page_name)
    else:
        return render(request, 'mySite/index.html')
    