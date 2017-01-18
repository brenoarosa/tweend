"""
"""

import pandas as pd
import numpy as np

from django.db.models import Count
from tweend.models import Tweet, ClassifiedTweet
from tweend.settings import BATCH_LENGTH, MAX_CLASSIFICATION_COUNT, COUNT_TEMP

def build_batch(user, batch_len=BATCH_LENGTH):
    """
    """

    tweets = Tweet.objects.all().annotate(classification_count=Count('classifiedtweet__id')).values_list('tweet_id', 'classification_count')

    classified_by_user = ClassifiedTweet.objects.filter(user=user).values_list('tweet_id', flat=True)
    maximum_classification_reached = tweets.filter(classification_count__gte=MAX_CLASSIFICATION_COUNT).values_list('tweet_id', flat=True)

    rejected_tweets = set(classified_by_user)
    rejected_tweets.update(maximum_classification_reached)

    df = pd.DataFrame.from_records(list(tweets))
    df.columns = ["tweet_id", "classification_count"]

    # p = 1 / (1 + e^(-t*count))
    df["p"] = 1 / (1 + np.exp(-df["classification_count"] * COUNT_TEMP))

    # removes probability for tweets we dont want anymore classification
    df["p"] = df["p"] * ~df["tweet_id"].isin(rejected_tweets)

    # normalize p
    df["p"] = df["p"] / sum(df["p"])

    # count tweets with p > 0
    valid_choices = df["p"].astype(bool).sum()

    if batch_len > valid_choices:
        batch_len = valid_choices

    selected_tweets = df.sample(n=batch_len, weights=df["p"])["tweet_id"]
    return Tweet.objects.filter(tweet_id__in=selected_tweets)
