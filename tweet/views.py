from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required

from tweet.models import Tweet
from tweet.forms import TweetAddForm
from twitteruser.views import profile_view
# Create your viedef index(request):


@login_required
def index(request):
    data = Tweet.objects.all()
    return render(request, 'index.html', {'data': data})


def Tweet_detail(request, tweet_id):
    tweet = Tweet.objects.filter(id=tweet_id).first()
    return render(request, "tweet_detail.html", {"tweet": tweet})


def NewTweet(request):
    html = "generic_form.html"

    if request.method == 'POST':
        form = TweetAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            make_tweet = Tweet.objects.create(
                tweet=data['tweet'],
                site_user=request.user,
            )
            # find_users = re.findall(r'@(\w+)', data['tweet'])
            # if '@' in data['tweet']:
            #     for users in find_users:
            #             Notification.objects.create(
            #                 current_user=TwitterUser.objects.get(username=users),
            #                 tweet=Tweet.object.filter(body=make_tweet).first()
            #             )
            return HttpResponseRedirect(reverse('homepage'))

    form = TweetAddForm()

    return render(request, html, {"form": form})
