from django.urls import path
from direct.views import inbox, Directs, SendDirect, UserSearch, NewConversation, reportIssue

# , NewPost, PostDetails, tags, like, favorite

urlpatterns = [
    path('', inbox, name='inbox'),
    path('directs/<username>', Directs, name='directs'),
    path('send/', SendDirect, name='send_directs'),
    path('new/', UserSearch, name='usersearch'),
    path('new/<username>', NewConversation, name='newconversation'),
    path('new/admin', reportIssue, name='reportIssue'),
]
