from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.

class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']

    def get_queryset(self):
        return BlogPost.objects.filter(published_date__isnull=False)

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'

class BlogPostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        form.instance.publish()  # Publish the post after creation
        return response

class BlogPostUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

    def get_queryset(self):
        return BlogPost.objects.filter(author=self.request.user)

class BlogPostDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def get_queryset(self):
        return BlogPost.objects.filter(author=self.request.user)
