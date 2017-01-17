"""
Tweet related models
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import ugettext as _


class Tweet(models.Model):
    """
    Unclassified Tweet Model
    """

    tweet_id = models.BigIntegerField(primary_key=True,
                                      verbose_name=_("Tweet ID"))
    created_at = models.DateTimeField(null=True,
                                      blank=True,
                                      verbose_name=_("Created at"))
    screen_name = models.CharField(max_length=15,
                                   null=True,
                                   blank=True,
                                   verbose_name=_("User's @"))
    text = models.CharField(max_length=140,
                            verbose_name=_("Tweet"))
    valid = models.BooleanField(default=True,
                                verbose_name=_("Valid"))
    displayed_count = models.IntegerField(default=0,
                                          verbose_name=_("Displayed Count"))

    @property
    def report_count(self):
        return TweetReport.objetcs.filter(tweet=self).count()


class ClassifiedTweet(models.Model):
    """
    Classified Tweet Model
    """

    tweet = models.ForeignKey(Tweet,
                              on_delete=models.CASCADE,
                              verbose_name=_("Tweet"))
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=True,
                             blank=True,
                             verbose_name=_("User"))
    classified_at = models.DateTimeField(default=timezone.now,
                                         null=True,
                                         blank=True,
                                         verbose_name=_("Created at"))
    NEGATIVE = 0
    NEUTRAL = 1
    POSITIVE = 2

    CLASS_CHOICES = (
        (NEGATIVE, _("Negative")),
        (NEUTRAL, _("Neutral")),
        (POSITIVE, _("Positive")),
    )

    classification = models.IntegerField(choices=CLASS_CHOICES,
                                         verbose_name=_("Classification"))


class TweetReport(models.Model):
    """
    Reports
    """
    tweet = models.ForeignKey(Tweet,
                              on_delete=models.CASCADE,
                              verbose_name=_("Tweet"))
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=True,
                             blank=True,
                             verbose_name=_("User"))
    displayed_at = models.DateTimeField(default=timezone.now,
                                        null=True,
                                        blank=True,
                                        verbose_name=_("Created at"))
