from django.shortcuts import render, get_object_or_404
from .models import Post, Category


# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {"page_name": "Blog", "posts": posts})


def category(request, category_id):
    cat = get_object_or_404(Category, id=category_id)
    return render(request, 'blog/category.html', {"page_name": "Blog", "category": cat})
