from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1) # status=1 means that the post is published, status=0 means that the post is draft.
    template_name = "post_list.html" # This is the template that will be used to render the view.