from django.shortcuts import render, get_object_or_404
from .models import Post, FirstPageQuotes
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
import random

def home(request):
    context = {
        'posts': Post.objects.all(),
        'quote': FirstPageQuotes.objects.last(),
    }
    return render(request, 'blog/index.html')


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        # context['posts'] = Post.objects.all()[::-1]
        context_all_quotes = FirstPageQuotes.objects.all()
        context_random_quotes = random.choice(context_all_quotes)
        context['quote'] = context_random_quotes
        context['title'] = 'Homepage'
        return context


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context1 = Post.objects.all()
        context2 = random.choice(context1)
        context3 = random.choice(context1)
        context['random_post'] = context2
        context['random_post2'] = context3
        post = get_object_or_404(Post, pk=self.kwargs['pk'], )
        context['title'] = post.title
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About Us'})
