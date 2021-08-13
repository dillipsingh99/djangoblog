from django.urls import path
from . views import (
    bloglistview, 
    blogdetailview, 
    BlogCreateView, 
    BlogUpdateView,
    BlogDeleteView,
    )

urlpatterns = [
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
    path('blog/<int:pk>/edit', BlogUpdateView.as_view(), name='blog_edit'),
    path('blog/new/', BlogCreateView.as_view(), name='blog_new'),
    path('blog/<int:_id>', blogdetailview, name='blog_datail'),
    path('', bloglistview, name='home'),
]