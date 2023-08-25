from django.urls import path
from blog.views import blog,blog_details

urlpatterns = [
    path('',blog,name='blog'),
    path('blog_details/',blog_details,name='blog_details'),
]
