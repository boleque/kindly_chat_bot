import random
from collections import namedtuple
from django.db import models
from django.contrib.postgres.fields import JSONField
from Levenshtein import distance


MIN_DISTANCE = 1 # Regulates "close enough". The larger the value the greater the margin of error and vice versa
# It would be nice to be able to update it 'on fly' (store it in db, for instance)
# I've defined it here for simplicity

Reply = namedtuple('Reply',['id','text'])  

class DialogueTypes(models.TextChoices):
    SAMPLES = 'SAMPLES', 'Samples'
    KEYWORDS = 'KEYWORDS', 'Keywords'

class CommonResponse(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    replies = models.JSONField()

    class Meta:
        abstract = True

class GreetingManager(models.Manager):
    def get_greeting_reply(self, language):
        greetingObj = super().get_queryset().get(pk='ae9c6010-85a2-4920-9ac5-35573eca5540')
        return Reply(None, random.choice(greetingObj.replies[language]))

class Greeting(CommonResponse):
    objects = GreetingManager()

class FallbackManager(models.Manager):
    def get_fallback_reply(self, language):
        query = super().get_queryset().get(pk='bd19343d-f298-4859-8002-cca5921b05a3')
        return Reply(id=None,  text=query.replies[language][0])

class Fallback(CommonResponse):
    objects = FallbackManager()

class DialogueManager(models.Manager):

    def get_dialogue_reply(self, message, language, last_reply_id=None):
        if last_reply_id is None:
            querySet = super().get_queryset()
        else:
            querySet = super().get_queryset().filter(parent_id=last_reply_id) or super().get_queryset()

        # from SAMPLES we opt a query with the most minimal distance
        sampleQueriesGen = (q for q in querySet if q.dialogue_type == DialogueTypes.SAMPLES)
        minDistance, targetQuery = float('inf'), None
        for query in sampleQueriesGen:
            newDistance = min(distance(s, message) for s in query.samples[language])
            if MIN_DISTANCE >= newDistance and minDistance > newDistance:
                minDistance, targetQuery = newDistance, query

        # if search through the SAMPLES failed, we'll choose a first complete match with KEYWORDS
        if targetQuery is None:
            keyWordQueriesGen = (q for q in querySet if q.dialogue_type == DialogueTypes.KEYWORDS)
            for query in keyWordQueriesGen:
                if message in query.keywords[language]:
                    targetQuery = query
                    break

        if targetQuery is not None:
            return Reply(
                id=targetQuery.pk, 
                text=random.choice(targetQuery.replies[language])
                )

        return None

class Dialogue(CommonResponse):
    parent_id = models.CharField(max_length=100, default=str)
    dialogue_type = models.CharField(max_length=20, choices=DialogueTypes.choices)
    keywords = models.JSONField(default=dict)
    samples = models.JSONField(default=dict)

    objects = DialogueManager()