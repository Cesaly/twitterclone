from django.shortcuts import render, reverse, HttpResponseRedirect
# from twitterclone import settings
from twitteruser.models import TwitterUser
from tweet.models import Tweet


# Create your views here.
# def index(request):
#     auth_value = settings.AUTH_USER_MODEL
#     return render(request, 'index.html', {'auth_value': auth_value})

def profile_view(request, current_id):
    html = 'profile.html'
    current_user = TwitterUser.objects.get(id=current_id)
    tweets = Tweet.objects.filter(site_user=current_user)
    follwers = current_user.following.count()
    return render(request, html, {
        'tweets': tweets, 'current_user': current_user, 'count': len(tweets), 'followers': follwers})


def follow_view(request, id):
    current_user = request.user
    follow_user = TwitterUser.objects.get(id=id)
    current_user.following.add(follow_user)
    current_user.save()
    return HttpResponseRedirect(reverse('homepage'))


def unfollow_view(request, id):
    current_user = request.user
    follow_user = TwitterUser.objects.get(id=id)
    current_user.following.remove(follow_user)
    current_user.save()
    return HttpResponseRedirect(reverse('homepage'))
