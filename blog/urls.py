from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogPostListView.as_view(), name='blogs'),
    path('<int:pk>', views.BlogPostDetailView.as_view(), name='blog-detail'),
    path('<int:pk>/create', views.CommentCreateView.as_view(), name='comment-create'),
    path('bloggers/', views.BlogAuthorListView.as_view(), name='bloggers'),
    path('bloggers/<int:pk>', views.BlogAuthorDetailView.as_view(), name='blogger-detail'),
]
