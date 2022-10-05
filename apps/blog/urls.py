from django.urls import path
from apps.blog.views import home, post_detail, posts_by_category


urlpatterns = [
    path('', home, name='home'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', post_detail, name='post_detail'),
    path('category/<slug:category>/', posts_by_category, name='posts_by_category'),
]