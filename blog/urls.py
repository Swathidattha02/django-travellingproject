from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogPostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.BlogPostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.BlogPostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', views.BlogPostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.BlogPostDeleteView.as_view(), name='post_delete'),
] 