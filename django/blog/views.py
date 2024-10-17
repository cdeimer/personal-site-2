from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import generic

from .models import Post

# Create your views here.

def index(request):
    latest_post_list = Post.objects.order_by("-date_posted")[:5]
    context = {
        "latest_post_list": latest_post_list,
    }
    return render(request, "blog/index.html", context)

class IndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "latest_post_list"

    def get_queryset(self):
        return Post.objects.order_by("-date_posted")[:5]

class DetailView(generic.DetailView):
    model = Post
    template_name = "blog/detail.html"