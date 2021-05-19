from django.urls import path
from direct.views import inbox, Directs, SendDirect

# , NewPost, PostDetails, tags, like, favorite

urlpatterns = [
    path('', inbox, name='inbox'),
    path('directs/<username>', Directs, name='directs'),
    path('send/', SendDirect, name='send_directs'),

]
