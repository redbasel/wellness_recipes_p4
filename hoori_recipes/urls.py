from . import views
from django.urls import path
# Trial importing new view
from .views import PostCreateView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    #Trial postCreate
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    #path('/post/new/', PostCreateView.as_view(), name='post_create'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]

