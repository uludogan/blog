
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView  # new
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # new

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):  # new
    model = Post
    template_name = "post_detail.html"

class BlogCreateView(CreateView):  # new
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]

class BlogUpdateView(UpdateView):  # new
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]
    
class BlogDeleteView(DeleteView):  # new
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")