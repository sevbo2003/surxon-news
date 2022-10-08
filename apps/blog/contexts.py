from apps.blog.models import Post


def get_posts(request):
    latest_posts = Post.objects.order_by('-created_at')
    posts_count = latest_posts.count()
    top_posts = Post.objects.order_by('-views')
    random_posts = Post.objects.order_by('?')[:6]
    return {'latest_posts': latest_posts, 'top_posts': top_posts, 'posts_count': posts_count, 'random_posts': random_posts}