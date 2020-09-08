from django import forms
from tweet.models import Tweet


class TweetAddForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = [
            'tweet'
        ]
