from django.urls import path
from apps.blog.views import home, post_detail


urlpatterns = [
    path('', home, name='home'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', post_detail, name='post_detail'),
]