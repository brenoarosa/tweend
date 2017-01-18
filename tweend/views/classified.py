"""
TweetClassified viewset
"""

from rest_framework import viewsets, permissions
from tweend.models import ClassifiedTweet
from tweend.serializers import ClassifiedTweetSerializer


class ClassifiedTweetViewSet(viewsets.ModelViewSet):
    queryset = ClassifiedTweet.objects.all()
    serializer_class = ClassifiedTweetSerializer
    permission_classes = (permissions.IsAuthenticated,)


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serialzier):
        serializer.save(user=self.request.user)
