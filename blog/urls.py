from django.urls import include, path
from . import views
from .views import PostList, PostDetail, PostNew, PostUpdate, PostDelete, PostShow, CommentCreateView, Dashboard, signup, signout

urlpatterns = [
	path('', views.PostShow.as_view(), name='home'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/new/', views.PostNew.as_view(), name='post_new'),
    path('post/<int:pk>/edit', views.PostUpdate.as_view(), name='post_edit'),
    path('post/<int:pk>/delete', views.PostDelete.as_view(), name='post_delete'),
    path('accounts/profile/', Dashboard, name='dashboard'),
    path('account/', include("django.contrib.auth.urls")),
     path('post/', views.PostList.as_view(), name='index'),
    path('accounts/signup/', signup, name='signup'),
    path('accounts/logout/', signout, name='logout'),
    path('post/<int:pk>/comment/', views.CommentCreateView.as_view(), name='comment_new'),
]