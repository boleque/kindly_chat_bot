import json
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from ..models import Conversation


class PublicConverationApiTest(TestCase):

    fixtures = ['kindly-bot.json']

    def setUp(self):
        self.client = APIClient()
        
        model = Conversation.objects.create(
            language='en'
        )

    def test_start_endpoint_http_201(self):
        input_data = {'language':'en'}
    
        response = self.client.post('/api/conversation/start/', json.dumps(input_data), content_type='json')
        self.assertEqual(response.status_code, 201)

    def test_start_endpoint_http_400(self):
        input_data = {'message':'Hello'}

        response = self.client.post('/api/conversation/start/', json.dumps(input_data), content_type='json')
        self.assertEqual(response.status_code, 400)

    # --------------------------------------------------

    def test_message_endpoint_http_200(self):
        input_data = {
            'user_id': 3, 
            'message':'Do you know any robot jokes?'
            }

        response = self.client.post('/api/conversation/message/', json.dumps(input_data), content_type='json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data['message'] in [
            "Do you know why robots take summer holidays? To charge the batteries!",
            "What do you call a pirate robot? Arrr2D2!",
            "What is a Robot's Favorite Music? Heavy metal!",
            "Why did the robot start school again? He had become quite rusty ...",
            "Why does a robot never get nervous? Because it has nerves of steel .."]
            )

    def test_message_endpoint_http_404(self):
        input_data = {
            'user_id': 250, 
            'message':'Hello'
            }

        response = self.client.post('/api/conversation/message/', json.dumps(input_data), content_type='json')
        self.assertEqual(response.status_code, 404)

    def test_message_endpoint_http_400(self):
        input_data = {
            'message':'I hope you know a couple of robot jokes?'
            }

        response = self.client.post('/api/conversation/message/', json.dumps(input_data), content_type='json')
        self.assertEqual(response.status_code, 400)