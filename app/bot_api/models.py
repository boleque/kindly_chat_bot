from django.db import models, migrations
from django.contrib.postgres.fields import HStoreField


class CommonResponse(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    replies = HStoreField()

    class Meta:
        abstract = True

class Greeting(CommonResponse):
    pass

class Fallback(CommonResponse):
    pass

class DialogueTypes(models.TextChoices):
    SAMPLES = 'SAMPLES', 'samples'
    KEYWORDS = 'KEYWORDS', 'keywords'

class Dialogue(CommonResponse):
    parent_id = models.CharField(max_length=100, default=str)
    dialogue_type = models.CharField(max_length=20, choices=DialogueTypes.choices)
    keywords = HStoreField(default=dict)
    samples = HStoreField(default=dict)

class Language(models.TextChoices):
    ENGLISH = 'en', 'English'
    NORWEGIAN = 'nb', 'Norwegian'

class Chat(models.Model):
    user_id = models.IntegerField(primary_key=True)
    language = models.CharField(max_length=20, choices=Language.choices)
    last_reply_id = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_language_valid",
                check=models.Q(language__in=Language.values),
            )
        ]