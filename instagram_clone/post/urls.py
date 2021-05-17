from django.urls import path
from post.views import index, NewPost, PostDetails

# , NewPost, PostDetails, tags, like, favorite

urlpatterns = [
    path('', index, name='index'),
    path('newpost/', NewPost, name='newpost'),
    path('<uuid: post_id>', PostDetails, name='postdetails'),

]
