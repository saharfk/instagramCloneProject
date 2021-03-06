from django.urls import path
from post.views import index, NewPost, PostDetails, tags, like, favorite, favoriteIn, likeIn

urlpatterns = [
    path('', index, name='index'),
    path('newpost/', NewPost, name='newpost'),
    path('<uuid:post_id>', PostDetails, name='postdetails'),
    path('tag/<slug:tag_slug>', tags, name='tags'),
    path('<uuid:post_id>/like', like, name='postlike'),
    path('<uuid:post_id>/post', likeIn, name='postlikeIn'),
    path('<uuid:post_id>/favorite', favorite, name='postfavorite'),
    path('<uuid:post_id>/favorite', favoriteIn, name='postfavoriteIn'),

]
