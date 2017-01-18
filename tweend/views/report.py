"""
TweetReport viewset
"""

from rest_framework import viewsets, permissions
from tweend.models import TweetReport
from tweend.serializers import TweetReportSerializer


class TweetReportViewSet(viewsets.ModelViewSet):
    queryset = TweetReport.objects.all()
    serializer_class = TweetReportSerializer
    permission_classes = (permissions.IsAuthenticated,)


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serialzier):
        serializer.save(user=self.request.user)
