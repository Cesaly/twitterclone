from django.db import models
from twitteruser.models import TwitterUser
# Create your models here.


class Tweet(models.Model):
    tweet = models.CharField(max_length=140)
    time_posted = models.DateTimeField(auto_now_add=True)
    site_user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.tweet
