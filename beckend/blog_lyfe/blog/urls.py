from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, BlogPostDestaqueView,BlogPostCategoriaView

urlpatterns = [
    path('',BlogPostListView.as_view()),
    path('destaque',BlogPostDestaqueView.as_view()),
    path('categoria',BlogPostCategoriaView.as_view()),
    path('<slug>',BlogPostDetailView.as_view()),
]
