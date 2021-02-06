from django.test import TestCase
from ..serializers import StartConversationSerializer, KeepConversationSerializer

class SerializersTests(TestCase):

    def test_valid_start_conversation_serializer(self):
        data = {
            "language": "en",
        }

        serializer = StartConversationSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_start_conversation_serializer(self):
        data = {
            "reply_id": "1-222-33",
            "message": "Hallo",
        }

        serializer = StartConversationSerializer(data=data)
        self.assertFalse(serializer.is_valid())
    
    def test_create_model_start_conversation_serializer(self):
        data = {
            "language": "nb",
            "last_reply_id": "test_id_0001"
        }

        serializer = StartConversationSerializer(data=data)
        serializer.is_valid()
        model = serializer.save()
        self.assertEqual(model.language, "nb")
        self.assertEqual(model.last_reply_id, "")

    # --------------------------------------------------

    def test_valid_keep_conversation_serializer(self):
        data = {
            "user_id": 1,
            "message": "Do you know and robot jokes?"
        }
        serializer = KeepConversationSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_no_user_id_invalid_keep_conversation_serializer(self):
        data = {
            "message": "Do you know and robot jokes?"
        }
        serializer = KeepConversationSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_user_id_invalid_keep_conversation_serializer(self):
        data = {
            "user_id": -1,
            "message": "Do you know and robot jokes?"
        }
        serializer = KeepConversationSerializer(data=data)
        self.assertFalse(serializer.is_valid())
