"""
URLs dispatcher
"""

import logging
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from tweend import views

logger = logging.getLogger(__name__)

router = DefaultRouter()
router.register(r'tweet', views.TweetViewSet)
router.register(r'report', views.TweetReportViewSet)
router.register(r'classified', views.ClassifiedTweetViewSet)

urlpatterns = [
    url(r'^$', views.HelloView.as_view(), name="index"),
    url(r'^api/1/classification/$', views.ClassificationAPIView.as_view(), name="classification"),
    url(r'^api/1/', include(router.urls)),
]
