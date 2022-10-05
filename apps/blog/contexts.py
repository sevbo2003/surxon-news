from apps.blog.models import Post


def get_posts(request):
    latest_posts = Post.objects.order_by('-created_at')
    top_posts = Post.objects.order_by('-views')
    return {'latest_posts': latest_posts, 'top_posts': top_posts}