from django.test import TestCase
from django.db.utils import IntegrityError
from .. models import Greeting, Dialogue

class ModelsTests(TestCase):

    fixtures = ['kindly-bot.json']

    def setUp(self):
        self.greeting = {
            'id': 'test-85a2-4920-9ac5-35573eca5540',
            'replies': {
                'en': [
                    "Hello! I am a chatbot!",
                ],
                "nb": [
                    "Hallo! Jeg er en chatbot!",
                ]
            }
        }

        self.dialogue = {
            "id": "test-15aa-4e30-8da1-f0af73466b0b",
            "dialogue_type": "SAMPLES",
            "samples": {
                "en": [
                    "Alright then",
                    "Pretty decent stuff",
                    "Oh well",
                ],
                "nb": [
                    "OK",
                    "null stress",
                    "herlig",
                    "javel",
                ]
            },
            "replies": {
                "en": [
                    "Is there anything else you need help with?",
                ],
                "nb": [
                    "Er det noe mer du trenger hjelp med?",
                ]
            }
        }

    def test_create_greeting_model_success(self):
        greetingObj = Greeting.objects.create(**self.greeting)
        self.assertEqual(greetingObj.id, self.greeting['id'])

    def test_get_greeting_reply_success(self):
        Greeting.objects.create(**self.greeting)
        reply = Greeting.objects.get_greeting_reply('en')
        self.assertTrue(reply.text in ["Hello! I am a chatbot!", "Hi there!"])

    def test_create_dialogue_model_success(self):
        greetingObj = Dialogue.objects.create(**self.dialogue)
        self.assertEqual(greetingObj.id, self.dialogue['id'])

    def test_get_dialogue_by_last_reply_id(self):
        reply = Dialogue.objects.get_dialogue_reply(
            message="Need to know more",
            language="en",
            last_reply_id='c6979e1f-f202-4330-8c63-d65f3b0c941a'
        )
        self.assertEqual(reply.text, "Ask away! I'm here to answer your questions.")

    def test_get_dialogue_by_keywords(self):
        reply = Dialogue.objects.get_dialogue_reply(
            message="NLU",
            language="nb",
        )
        self.assertEqual(reply.text, \
            'Kindlys chatboter er intelligente fordi de bruker maskinlæring, en teknologi som lar dem lære fra data. Dette gjør det mulig for datamaskiner å lære naturlig språk ved å se på faktiske eksempler i språket. Litt som oss mennesker!')

    def test_get_dialogue_by_samples(self):
        reply = Dialogue.objects.get_dialogue_reply(
            message="You're a cool bot",
            language="en",
        )

        self.assertTrue(reply.text in ["I try my best. 😊", "So nice to hear. 😊", "Thanks, that's kind of you. 😊"])

