"""
Tweend settings and default values
"""

from django.conf import settings


BATCH_LENGTH = getattr(settings, 'BATCH_LENGTH', 30)
MAX_CLASSIFICATION_COUNT = getattr(settings, 'MAX_CLASSIFICATION_COUNT', 3)
COUNT_TEMP = getattr(settings, 'COUNT_TEMP', 100)
