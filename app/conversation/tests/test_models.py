from django.test import TestCase
from django.db.utils import IntegrityError
from .. models import Conversation

class ModelsTests(TestCase):

    def test_create_conversation_model_success(self):

        input_data = {'language': 'en'}
        conversation = Conversation.objects.create(
            language=input_data['language']
        )
        self.assertEqual(conversation.language, input_data['language'])