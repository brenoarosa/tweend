"""
Tweet Patch Classification view
"""

from rest_framework import views, permissions, status
from rest_framework.response import Response
from tweend.models import Tweet, ClassifiedTweet
from tweend.serializers import TweetSerializer, ClassifiedTweetSerializer
from tweend.utils import build_patch


class ClassificationAPIView(views.APIView):

    allowed_methods = ('GET', 'POST')
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        tweet_qs = build_patch(request.user)
        serializer = TweetSerializer(tweet_qs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClassifiedTweetSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
