from django.db import models

class Language(models.TextChoices):
    ENGLISH = 'en', 'English'
    NORWEGIAN = 'nb', 'Norwegian'

class Conversation(models.Model):
    user_id = models.AutoField(primary_key=True)
    language = models.CharField(max_length=20, choices=Language.choices)
    last_reply_id = models.CharField(max_length=100, blank=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_language_valid",
                check=models.Q(language__in=Language.values),
            )
        ]
    
    def __str__(self):
        return "user_id={}; language={}; last_reply_id={}".format(
            self.user_id,
            self.language, 
            self.last_reply_id
        )