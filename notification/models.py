from django.db import models
from tweet.models import Tweet
from twitteruser.models import TwitterUser
# Create your models here.

# User for whoever the notication belongs to, body aka the tweet, has the user seen it yes or no
class NotifyItem(models.Model):
    user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    body = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    seen = models.BooleanField()

    def __str__(self):
        return self.TwitterUser.name
