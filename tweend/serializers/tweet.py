"""
Tweet serializers
"""

from rest_framework import serializers
from tweend.models import Tweet, ClassifiedTweet, TweetReport


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('tweet_id', 'created_at', 'screen_name', 'text', 'valid')


class ClassifiedTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassifiedTweet
        fields = ('tweet', 'user', 'classified_at', 'classification')


class TweetReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetReport
        fields = ('tweet', 'user', 'displayed_at')
