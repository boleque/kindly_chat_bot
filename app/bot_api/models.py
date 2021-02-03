from django.db import models, migrations
from django.contrib.postgres.fields import HStoreField
from model_utils import Choices


class CommonResponse(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    replies = HStoreField()

    class Meta:
        abstract = True

class Greeting(CommonResponse):
    pass

class Fallback(CommonResponse):
    pass

class Dialogue(CommonResponse):
    parent_id = models.CharField(max_length=100, default=str)
    dialogue_type = models.CharField(max_length=20, choices=Choices('SAMPLES', 'KEYWORDS'))
    keywords = HStoreField(default=dict)
    samples = HStoreField(default=dict)