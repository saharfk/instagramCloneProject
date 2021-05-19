from django.urls import path
from direct.views import inbox

# , NewPost, PostDetails, tags, like, favorite

urlpatterns = [
    path('', inbox, name='inbox'),

]
