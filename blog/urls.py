from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views
from .views import PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='about')
]

# >>> import json
# >>> from blog.models import Post
# with open('posts.json') as f:
# ...     posts_json = json.load(f)
# ...
# >>> for post in posts_json:
# ...     post = Post(title=post['title'], content=post['content'], author_id=post['user_id'])
# ...     post.save()
# ... exit()