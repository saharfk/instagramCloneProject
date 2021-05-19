from django.template import loader
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from direct.models import Message


# Create your views here.

@login_required
def inbox(request):
    messages = Message.get_messages(user=request.user)
    active_direct = None
    directs = None

    if messages:
        message = messages[0]
        active_direct = message['user'].username
        directs = Message.objects.filter(user=request.user, recipient=message['user'])
        directs.update(is_read=True)
        for message in messages:
            if message['user'].username == active_direct:
                message['unread'] = 0

    context = {
        'directs': directs,
        'messages': messages,
        'active_direct': active_direct,
    }

    template = loader.get_template('direct/direct.html')

    return HttpResponse(template.render(context, request))
