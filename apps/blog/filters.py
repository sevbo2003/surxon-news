import django_filters
from apps.blog.models import Post


class PostSearchFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['title']