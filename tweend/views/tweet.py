"""
Tweet viewset
"""

from rest_framework import viewsets, permissions
from tweend.models import Tweet
from tweend.serializers import TweetSerializer


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = (permissions.IsAuthenticated,)
