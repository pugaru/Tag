from django.urls import path

from .views import HomepageView, PageView, TagView, tag_list, CategoryView

from . import views

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage-view'),
    path('post/<int:pk>', views.PhotoView.as_view(), name='photo-detail'),
    path('tags/', tag_list, name='tag-list'),
    path('tag/<str:tag>/', TagView.as_view(), name='tag-view'),
    path('<slug:slug>/', PageView.as_view(), name='page-view'),
    path('category/<slug:slug>/', CategoryView.as_view(), name='category-view'),
]
