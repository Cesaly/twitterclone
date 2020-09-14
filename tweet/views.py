from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin

from tweet.models import Tweet
from tweet.forms import TweetAddForm
from twitteruser.views import profile_view
# Create your viedef index(request):


# @login_required
# def index(request):
#     data = Tweet.objects.all()
#     return render(request, 'index.html', {'data': data})


class Alt_index(LoginRequiredMixin, View):
    def get(self, request):
        html = "index.html"

        data = Tweet.objects.all()

        return render(request, html, {"data": data})


# def Tweet_detail(request, tweet_id):
#     tweet = Tweet.objects.filter(id=tweet_id).first()
#     return render(request, "tweet_detail.html", {"tweet": tweet})


class TweetDetail(View):
    def get(self, request, tweet_id):
        html = 'tweet_detail.html'

        tweet = Tweet.objects.filter(id=tweet_id).first()

        return render(request, html, {"tweet": tweet})


# def NewTweet(request):
#     html = "generic_form.html"

#     if request.method == 'POST':
#         form = TweetAddForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             make_tweet = Tweet.objects.create(
#                 tweet=data['tweet'],
#                 site_user=request.user,
#             )
#             return HttpResponseRedirect(reverse('homepage'))

#     form = TweetAddForm()

#     return render(request, html, {"form": form})


class NewTweet(View):
    html = "generic_form.html"

    def get(self, request):
        form = TweetAddForm()
        return render(request, self.html, {"form": form})

    def post(self, request):
        form = TweetAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            make_tweet = Tweet.objects.create(
                tweet=data['tweet'],
                site_user=request.user,
            )
            return HttpResponseRedirect(reverse('homepage'))
        return render(request, self.html, {"form": form})
