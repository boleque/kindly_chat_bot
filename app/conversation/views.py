import json
from django.shortcuts import get_object_or_404
from django.http.response import Http404
from rest_framework import status, decorators, response, exceptions
from core.models import Greeting, Dialogue, Fallback
from . serializers import StartConversationSerializer, KeepConversationSerializer
from . models import Conversation

@decorators.api_view(['POST'])
def start_endpoint(request):

    serializer = StartConversationSerializer(
        data=json.loads(request.body.decode('utf-8'))
        )

    serializer.is_valid(raise_exception=True)
    conversationObj = serializer.save()
    reply = Greeting.objects.get_greeting_reply(conversationObj.language)

    return response.Response(
        data={
            'user_id' : conversationObj.user_id,
            'message' : reply.text,
            }, 
            status=status.HTTP_201_CREATED
            )

@decorators.api_view(['POST'])
def message_endpoint(request):

    serializer = KeepConversationSerializer(
        data=json.loads(request.body.decode('utf-8'))
        )

    try:
        if serializer.is_valid(raise_exception=True):

            validated_data = serializer.validated_data
            conversationObj = get_object_or_404(Conversation.objects.all(), user_id=validated_data['user_id'])
            user_language = conversationObj.language
            
            reply = Dialogue.objects.get_dialogue_reply(
                message=validated_data['message'],
                language=user_language,
                last_reply_id=conversationObj.last_reply_id or None,
                )

            if reply is not None:
                conversationObj.last_reply_id = reply.id
            else:
                reply = Fallback.objects.get_fallback_reply(user_language)

    except exceptions.ValidationError as err:

        return response.Response(
            data=err.get_full_details(), 
            status=status.HTTP_400_BAD_REQUEST
            )

    except Http404:

        return response.Response(
            data=serializer.data['user_id'], 
            status=status.HTTP_404_NOT_FOUND
            )

    else:

        return response.Response(
            data={
                'message': reply.text,
            }, 
            status=status.HTTP_200_OK
            )