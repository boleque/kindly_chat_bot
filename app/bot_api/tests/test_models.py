from django.test import TestCase
from django.db.utils import IntegrityError
from .. models import Chat

class ModelsTests(TestCase):

    def test_create_chat_model_success(self):

        input_data = {'user_id': 1, 'language': 'en'}
        chat = Chat.objects.create(
            user_id=input_data['user_id'],
            language=input_data['language']
        )
        self.assertEqual(chat.user_id, input_data['user_id'])
        self.assertEqual(chat.language, input_data['language'])
    
    def test_create_chat_model_wrong_lang(self):

        input_data = {'user_id': 1, 'language': 'FI'}
        chat = Chat(
            user_id=input_data['user_id'],
            language=input_data['language']
        )

        try:
            chat.save()
        except Exception as err:
            self.assertEqual(IntegrityError, type(err))

        #self.assertEqual(chat.user_id, input_data['user_id'])
        #self.assertEqual(chat.language, input_data['language'])