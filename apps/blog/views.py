from django.shortcuts import render, get_object_or_404
from apps.blog.models import Post, Category
from apps.blog.filters import PostSearchFilter
from django.utils import timezone
from datetime import timedelta


def home(request):
    search = request.GET.get('qidirish')
    if search:
        posts = Post.objects.filter(title__icontains=search)
        return render(request, 'home.html', {'posts': posts})
    return render(request, 'home.html')
    

def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, created_at__year=year, created_at__month=month, created_at__day=day)
    post.views += 1
    post.save()
    context = {
        'post': post,
    }
    return render(request, 'post_detail.html', context)


def posts_by_category(request, category):
    category1=Category.objects.get(slug=category)
    filter = request.GET.get('filter_by')
    categories = Category.objects.all()
    if filter:
        if filter == 'featured':
            posts = Post.objects.filter(category__slug=category, featured=True)
        elif filter == 'popular':
            posts = Post.objects.filter(category__slug=category).order_by('-views')
        elif filter == 'popular7days':
            try:
                posts = Post.objects.filter(category__slug=category, created_at__gte=timezone.now() - timedelta(days=7)).order_by('-views')
            except:
                posts = Post.objects.filter(category__slug=category)
        elif filter == 'random_posts':
            posts = Post.objects.filter(category__slug=category).order_by('?')
        return render(request, 'posts_by_category.html', {'posts': posts})
    posts = Post.objects.filter(category__slug=category)
    return render(request, 'posts_by_category.html', {'posts': posts, 'categories': categories, 'category1': category1})