from django.http import HttpResponseRedirect


def custom_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('post')
    else:
        return HttpResponseRedirect('user/login')
